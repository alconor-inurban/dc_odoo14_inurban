# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#
# Please note that these reports are not multi-currency !!!
#

import re

from odoo import api, fields, models, tools
from odoo.exceptions import UserError
from odoo.osv.expression import expression


class SampleReport(models.Model):
    _name = "sample.report"
    _description = "Sample Report"
    _auto = False
    _order = 'date_order desc, price_total desc'

    date_order = fields.Datetime('Order Date', readonly=True, help="Depicts the date when the Quotation should be validated and converted into a purchase order.")
    state = fields.Selection([
        ('draft', 'Draft RFQ'),
        ('sent', 'RFQ Sent'),
        ('to approve', 'To Approve'),
        ('sample', 'Sample Order'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], 'Status', readonly=True)
    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    partner_id = fields.Many2one('res.partner', 'Vendor', readonly=True)
    date_approve = fields.Datetime('Confirmation Date', readonly=True)
    product_uom = fields.Many2one('uom.uom', 'Reference Unit of Measure', required=True)
    company_id = fields.Many2one('res.company', 'Company', readonly=True)
    currency_id = fields.Many2one('res.currency', 'Currency', readonly=True)
    user_id = fields.Many2one('res.users', 'Purchase Representative', readonly=True)
    delay = fields.Float('Days to Confirm', digits=(16, 2), readonly=True, help="Amount of time between purchase approval and order by date.")
    delay_pass = fields.Float('Days to Receive', digits=(16, 2), readonly=True, help="Amount of time between date planned and order by date for each purchase order line.")
    avg_days_to_purchase = fields.Float(
        'Average Days to Purchase', digits=(16, 2), readonly=True, store=False,  # needs store=False to prevent showing up as a 'measure' option
        help="Amount of time between purchase approval and document creation date. Due to a hack needed to calculate this, \
              every record will show the same average value, therefore only use this as an aggregated value with group_operator=avg")
    price_total = fields.Float('Total', readonly=True)
    price_average = fields.Float('Average Cost', readonly=True, group_operator="avg")
    nbr_lines = fields.Integer('# of Lines', readonly=True)
    category_id = fields.Many2one('product.category', 'Product Category', readonly=True)
    product_tmpl_id = fields.Many2one('product.template', 'Product Template', readonly=True)
    country_id = fields.Many2one('res.country', 'Partner Country', readonly=True)
    fiscal_position_id = fields.Many2one('account.fiscal.position', string='Fiscal Position', readonly=True)
    account_analytic_id = fields.Many2one('account.analytic.account', 'Analytic Account', readonly=True)
    commercial_partner_id = fields.Many2one('res.partner', 'Commercial Entity', readonly=True)
    weight = fields.Float('Gross Weight', readonly=True)
    volume = fields.Float('Volume', readonly=True)
    order_id = fields.Many2one('sample.order', 'Sample Order', readonly=True)
    untaxed_total = fields.Float('Untaxed Total', readonly=True)
    qty_ordered = fields.Float('Qty Ordered', readonly=True)
    qty_received = fields.Float('Qty Received', readonly=True)
    qty_billed = fields.Float('Qty Billed', readonly=True)
    qty_to_be_billed = fields.Float('Qty to be Billed', readonly=True)
    product_qty = fields.Float(string='Peso M.E.', digits='Product Unit of Measure', required=True)

    def init(self):
        # self._table = sale_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            FROM ( %s )
            %s
            )""" % (self._table, self._select(), self._from(), self._group_by()))

    def _select(self):
        select_str = """SELECT 
            po.id as order_id,
            min(l.id) as id,
            po.name,
            po.date_order "FH Muestra",
            po.date_approve,
            co.fechahoracaptura "FH Guia", 
            co.fecha_guia, 
            co.hora_entrada, 
            co.dia_zafra ,
            co.lote_hora ,
            co.turno "Turno 12 Hrs",
            me.codigo_activo "Caja",
            (case WHEN me.codigo_activo = co.caja1 then co.alce1 else co.alce2 end) "EQUIPO CyA" ,
            (case WHEN me.codigo_activo = co.caja1 then co.epl_alce1 else co.epl_alce2 end) "Operador CyA" ,
            po.partner_id,
            partner.name "Proveedor",
            po.state "Estatus",
            po.guia,
            po.tickete,
            po.frente ,
            pp."name" "Nombre Proyecto" ,
            fpu."name" "UP",
            pp.lote,	
            fpv."name" "Variedad",
            fpt."name" "TDCorte",
            po.tipo_cane "Tipo Cania",
            po.hdc "FechaHora Corte",
            po.qty_total "Cant. Total",
            po.porc_impureza "_% Impur.",
            t.categ_id as category_id,
            pc."name" "Categoria",
            sum(l.price_subtotal / COALESCE(po.currency_rate, 1.0))::decimal(16,2) as untaxed_total,
            sum(l.price_total / COALESCE(po.currency_rate, 1.0))::decimal(16,2) as price_total,
            t.description "Nota/Causa",
            t.default_code "Código M.E.",
            l."name" "Nombre M.E.",
            l.product_qty ,
            l.porc_item "_% M.E.",
            l.longitud_avg "_Longitud"
        """
        return select_str

    def _from(self):
        from_str = """
        sample_order_line l
        join sample_order po on (l.order_id=po.id)
        join res_partner partner on po.partner_id = partner.id
            left join product_product p on (l.product_id=p.id)
                left join product_template t on (p.product_tmpl_id=t.id)
                	left join product_category pc on (pc.id=t.categ_id)
        left join uom_uom line_uom on (line_uom.id=l.product_uom)
        left join uom_uom product_uom on (product_uom.id=t.uom_id)
        left join project_project pp on (pp.id = po.projects_id)
        	left join fincas_pma_up fpu on (fpu.id = pp.up)
        left join fincas_pma_variedades fpv on (fpv.id = po.variedad)
        left join fincas_pma_tiposcortes fpt on (fpt.id = po.tipocorte)
        left join purchase_order co on (cast (co.secuencia_guia as VARCHAR ) = po.guia) 
        	left join maintenance_equipment me on (me.id=po.caja_muestra)
        """
        return from_str

    def _group_by(self):
        group_by_str = """
            GROUP BY
                po.id,
                co.fecha_guia,
                po.date_order ,
                po.date_approve,
                co.fechahoracaptura, 
                po.name,            
                co.hora_entrada, 
                co.dia_zafra ,
                co.lote_hora ,
                co.turno ,
                me.codigo_activo,
                co.caja1,
                co.caja2,
                co.alce1,
                co.alce2,
                co.epl_alce1,
                co.epl_alce2,
                partner.name ,
                po.state,
                po.guia,
                po.tickete,
                po.frente ,
                pp."name",
                fpu."name",
                pp.lote,
                fpv."name",
                fpt."name",
                po.tipo_cane ,
                po.hdc ,
                po.qty_total,
                po.porc_impureza ,
                t.categ_id,
                pc."name" ,
                t.description,
                t.default_code,
                l."name",
                l.product_qty,
                l.porc_item,
                l.longitud_avg
        """
        return group_by_str

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        """ This is a hack to allow us to correctly calculate the average of PO specific date values since
            the normal report query result will duplicate PO values across its PO lines during joins and
            lead to incorrect aggregation values.

            Only the AVG operator is supported for avg_days_to_purchase.
        """
        avg_days_to_purchase = next((field for field in fields if re.search(r'\bavg_days_to_purchase\b', field)), False)

        if avg_days_to_purchase:
            fields.remove(avg_days_to_purchase)
            if any(field.split(':')[1].split('(')[0] != 'avg' for field in [avg_days_to_purchase] if field):
                raise UserError("Value: 'avg_days_to_purchase' should only be used to show an average. If you are seeing this message then it is being accessed incorrectly.")

        res = []
        if fields:
            res = super(SampleReport, self).read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)

        if not res and avg_days_to_purchase:
            res = [{}]

        if avg_days_to_purchase:
            query = """ SELECT AVG(days_to_purchase.po_days_to_purchase)::decimal(16,2) AS avg_days_to_purchase
                          FROM (
                              SELECT extract(epoch from age(po.date_approve,po.create_date))/(24*60*60) AS po_days_to_purchase
                              FROM purchase_order po
                              WHERE po.id IN (
                                  SELECT "purchase_report"."order_id" FROM %s WHERE %s)
                              ) AS days_to_purchase
                    """

            subdomain = domain + [('company_id', '=', self.env.company.id), ('date_approve', '!=', False)]
            subtables, subwhere, subparams = expression(subdomain, self).query.get_sql()

            self.env.cr.execute(query % (subtables, subwhere), subparams)
            res[0].update({
                '__count': 1,
                avg_days_to_purchase.split(':')[0]: self.env.cr.fetchall()[0][0],
            })
        return res
