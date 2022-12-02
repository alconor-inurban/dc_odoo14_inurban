# -*- coding: utf-8 -*-
from odoo import models, fields, api
# HERENCIA - AMPLIANDO APLICACIONES EXISTENTES
#    AHORA AGREGAREMOS UNOS CAMPOS A UN MODELO EXISTENTE;  EN ESTE CASO SERIA EL MODELO
#    PROYECTO EL CAMPO A AGREGAR ES: fincas_pma EN EL NOMBRE DEL MODELO:
#    purchase.order ESTE SE BUSCA EN EL MENU: AJUSTES; OPCIN: TECNICO; SECCION:
#    SECUENCIA E IDENTIFICADRES
    
class GuiasPurchase_Order(models.Model):
    _inherit = 'purchase.order'
    
    
    active = fields.Boolean('Activo', default=True)
    secuencia_guia = fields.Integer(string="-Secuencia_guia")
    ano = fields.Char('-Año', tracking=True)
    zafra = fields.Many2one('fincas_pma.zafras', string = '-Zafra [Año]', tracking=True)
    fechahoracaptura = fields.Datetime('-Fecha y Hora de Captura', tracking=True, default=fields.Datetime.now)
    fechahc = fields.Char('-Fecha Hora Captura en String', tracking=True)
    placa = fields.Char(string='-Placa', tracking=True)
    tipo_equipo = fields.Many2one('fincas_pma.tipo_equipo', string= '-Tipo de Equipo', tracking=True)
    frente = fields.Many2one('fincas_pma.frentes', string = '-Frente', tracking=True)
    up = fields.Many2one('fincas_pma.up', string = '-U.P.', tracking=True)
    lote = fields.Char('-LOT', tracking=True, default='000')
    tipo_vehiculo = fields.Char('-Tipo Vehículo', tracking=True)
    contrato = fields.Char(string= '-Contrato', tracking=True)
    fecha_guia = fields.Date('-Fecha Guía', tracking=True)
    fecha_quema = fields.Date('-Fecha Quema', tracking=True)
    hora_quema = fields.Char('-Hora Quema', tracking=True)
    # 2020-12-23 - 10:20
    bruto = fields.Float("-Bruto [Lbs]", tracking=True)
    tara = fields.Float("-Tara [Lbs]", tracking=True)
    neto = fields.Float("-Neto [Lbs]", tracking=True)
    # 2021-01-06 - 10:50 - ALCE ,TRANSFERENCIA y ACARREO
    tipo_alce = fields.Char(string= '-Tipo_Alce', tracking=True)
    alce1 = fields.Char(string= '-Alce1', tracking=True)
    alce2 = fields.Char(string= '-Alce2', tracking=True)
    epl_alce1 = fields.Char(string= '-Empl. Alce1', tracking=True)
    epl_alce2 = fields.Char(string= '-Empl. Alce2', tracking=True)
    montacargas = fields.Char(string= '-Montacargas', tracking=True)
    epl_montacarga = fields.Char(string= '-Empl. Montacarga', tracking=True)
    tractor1 = fields.Char(string= '-Tractor 1', tracking=True)
    tractor2 = fields.Char(string= '-Tractor 2', tracking=True)
    epl_tractor1 = fields.Char(string= '-Empl. Tractor 1', tracking=True)
    epl_tractor2 = fields.Char(string= '-Empl. Tractor 2', tracking=True)
    nombre_tansportista = fields.Char(string= '-Nombre Transportista', tracking=True)
    num_epl_tansportista = fields.Char(string= '-Num. Empl. Transportista', tracking=True)
    neto_ton = fields.Float("-Neto [Tons C.]", tracking=True)
    ton1 = fields.Float("-Neto Caja 1[Tons]", tracking=True)
    ton2 = fields.Float("-Neto Caja 2[Tons]", tracking=True)
    cha1 = fields.Char(string= '-Chasis 1', tracking=True)
    tcha1 = fields.Char(string= '-Tara Chasis 1', tracking=True)
    cha2 = fields.Char(string= '-Chasis 2', tracking=True)
    tcha2 = fields.Char(string= '-Tara Chasis 2', tracking=True)
    mula = fields.Char(string= '-Mula', tracking=True)
    tmula = fields.Char(string= '-Tara Mula', tracking=True)
    chamula = fields.Char(string= '-Chasis Mula', tracking=True)
    tchamula = fields.Char(string= '-Tara Chasis Mula', tracking=True)
    caja1 = fields.Char(string= '-Caja 1', tracking=True)
    tcaja1 = fields.Char(string= '-Tara Caja 1', tracking=True)
    caja2 = fields.Char(string= '-Caja 2', tracking=True)
    tcaja2 = fields.Char(string= '-Tara Caja 2', tracking=True)
    promedio = fields.Float("-Promedio", tracking=True)
    dia_zafra = fields.Char("-Día Zafra ", tracking=True)
    detalle = fields.Char(string= '-Detalle', tracking=True)
    cerrado = fields.Boolean('-Cerrado', tracking=True)
    eliminado = fields.Boolean('-Eliminado', tracking=True)
    usuario_guia = fields.Char(string= '-Usuario Guía', tracking=True)
    procesado_contabilidad = fields.Boolean('-Procesado Contabilidad', tracking=True)
    hora_entrada = fields.Char('-Hora Entrada', tracking=True)
    hora_salida =  fields.Char('-Hora Salida', tracking=True)
    cerrado_total = fields.Boolean('-Cerrado Total', tracking=True)
    incetivo_tl = fields.Boolean('-Incentivo TL', tracking=True)
    incentivo_ti = fields.Boolean('-Incentivo TI', tracking=True)
    fecha_tiquete = fields.Char('-Fecha Tickete', tracking=True)
    hora_tiquete = fields.Char('-Hora Tickete', tracking=True)
    usuario_tiquete = fields.Char('-Usuario Tickete', tracking=True)
    origen_tiquete = fields.Char('-Origen Tickete', tracking=True)
    tipo_cane = fields.Selection([('PV','CAÑA PICADA VERDE'),('PQ','CAÑA PICADA QUEMADA'),('LV','CAÑA LARGA VERDE'),('LQ','CAÑA LARGA QUEMADA')], tracking=True)
    lote_hora = fields.Char('-Lote-Hora', tracking=True)
    # 2021-01-08 - 11:00
    cane = fields.Char('-Tipo Caña V/Q', tracking=True)
    neto_tonl = fields.Float("-Neto [Tons L.]", tracking=True)
    cant_cajas = fields.Integer(string="-Cant. Cajas", tracking=True)
    # 2021-01-09 - 04:15
    turno = fields.Char('-Turno', tracking=True)
    uplote = fields.Char(string='-UP.Lote', tracking=True, store=True, compute='_onchange_uplote', required=True)
    
    @api.depends('up','lote')
    def _onchange_uplote(self):
        lc_uplote = ''
        if not self.up:
            print('Sin UP', self.up)
            return lc_uplote
        else:
            self.uplote = self.up.code_up + '-' + self.lote
            lc_uplote = self.uplote
            print('Con UP:', lc_uplote)
        return lc_uplote    

class GuiasPurchase_OrderLine(models.Model):
    _inherit = 'purchase.order.line'

    active = fields.Boolean('Activo', default=True)
    secuencia_guia = fields.Integer(string="-Secuencia_guia")
    bruto = fields.Float("-Bruto [Lbs]", tracking=True)
    tara = fields.Float("-Tara [Lbs]", tracking=True)
    neto = fields.Float("-Neto [Lbs]", tracking=True)
    # 2021-02-13: 14:25
    contrato = fields.Many2one('maintenance.equipment',string="Equipo Acarreo:", tracking=True, required=True)
    alce = fields.Many2one('maintenance.equipment',string="Equipo CyA:", tracking=True, required=True)
    caja = fields.Many2one('maintenance.equipment',string="Equipo Caja:", tracking=True, required=True)
    project_id = fields.Many2one('project.project',string="Project")

    #id|
    # name|                     <> '[MP-001] CAÑA DE AZUCAR'
    # sequence|                 <> 10
    # product_qty|              <> lbs -> Kg x1.0
    # product_uom_qty|          <> lbs -> Kg x1.0 
    # date_planned|
    # product_uom|              <> 1
    # product_id|               <> 2 - [MP-001]
    # price_unit|               <> 0.00
    # price_subtotal|           <> 0.00
    # price_total|              <> 0.00
    # price_tax|                <> 0.00
    # order_id|                 <> viene del encabezado!!!
    # account_analytic_id|
    # company_id|               <> 1
    # state|                    <> 'purchase'
    # qty_invoiced|     
    # qty_received_method|      <> 'stock_moves'
    # qty_received|             <?> 0.00
    # qty_received_manual|      <?> 0.00
    # qty_to_invoice|
    # partner_id|               <> Proveedor
    # currency_id|              <> 16 ??
    # display_type|
    # create_uid|
    # create_date|
    # write_uid|
    # write_date|
    # sale_order_id|
    # sale_line_id|