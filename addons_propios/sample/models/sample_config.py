# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime, date, time, timedelta
import calendar
#from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from itertools import groupby
from pytz import timezone, UTC
from werkzeug.urls import url_encode

from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_is_zero
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang


class SampleConfig(models.TransientModel):
    _name = 'new_sample.config'
#    _inherit = 'res.config.settings'

    name = fields.Char('configuración de Muestras', default='sample config')
    peso_minimo_muestra = fields.Float('Peso Mínimo Muestra Caña Picada', tracking=True, store=True, default=65.00)
    weight_uom_name = fields.Char(string='Etiqueta de unidad de medida de peso', compute='_compute_weight_uom_name',store=False)
    peso_minimo_muestra_larga = fields.Float('Peso Mínimo Muestra Caña Larga', tracking=True, store=True, default=120.00)
    # ALERTAS DE TIEMPO DE CORTE
    alerta_ama_hora_verde = fields.Float('Alerta Amarilla Hrs Corte y Pesa de la Muestra Caña Verde', tracking=True, store=True, default = 10)
    alerta_roj_hora_verde = fields.Float('Alerta Roja Hrs Corte y Pesa de la Muestra Caña Verde', tracking=True, store=True, default = 12)
    alerta_ama_hora_quema = fields.Float('Alerta Amarilla Hrs Corte y Pesa de la Muestra Caña Qmda.', tracking=True, store=True, default = 30)
    alerta_roj_hora_quema = fields.Float('Alerta Roja Hrs Corte y Pesa de la Muestra Caña Qmda.', tracking=True, store=True, default = 36)
    # ALERTAS DE PORCENTAJE MATERIA EXTRAÑA
    alerta_ama_porc_verde = fields.Float('Alerta Amarilla % Materia Extraña de la Muestra Caña Verde', tracking=True, store=True, default = 11)
    alerta_roj_porc_verde = fields.Float('Alerta Roja % Materia Extraña de la Muestra Caña Verde', tracking=True, store=True, default = 16)
    alerta_ama_porc_quema = fields.Float('Alerta Amarilla % Materia Extraña de la Muestra Caña Qmda.', tracking=True, store=True, default = 8)
    alerta_roj_porc_quema = fields.Float('Alerta Roja % Materia Extraña de la Muestra Caña Qmda.', tracking=True, store=True, default = 13)

    def _compute_weight_uom_name(self):
        self.weight_uom_name = self._get_weight_uom_name_from_ir_config_parameter()

    @api.model
    def _get_weight_uom_name_from_ir_config_parameter(self):
        return self._get_weight_uom_id_from_ir_config_parameter().display_name

    @api.model
    def _get_weight_uom_id_from_ir_config_parameter(self):
        """ Get the unit of measure to interpret the `weight` field. By default, we considerer
        that weights are expressed in kilograms. Users can configure to express them in pounds
        by adding an ir.config_parameter record with "product.product_weight_in_lbs" as key
        and "1" as value.
        """
        product_weight_in_lbs_param = self.env['ir.config_parameter'].sudo().get_param('product.weight_in_lbs')
        if product_weight_in_lbs_param == '1':
            return self.env.ref('uom.product_uom_lb', False) or self.env['uom.uom'].search([('measure_type', '=' , 'weight'), ('uom_type', '=', 'reference')], limit=1)
        else:
            return self.env.ref('uom.product_uom_kgm', False) or self.env['uom.uom'].search([('measure_type', '=' , 'weight'), ('uom_type', '=', 'reference')], limit=1)
