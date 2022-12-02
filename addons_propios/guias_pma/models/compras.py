# -*- coding: utf-8 -*-
from odoo import models, fields, api
from openerp import exceptions
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
#from odoo.exceptions import AccessError, UserError, ValidationError
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
    uplote = fields.Char(string='-UP.Lote', tracking=True, store=True, compute='_onchange_uplote', required=False)
    # 2021-03-02 - 19:13 [Mismo modelo]
    project_id = fields.Many2one('project.project',string="Project", default=1)

    def _compute_jocker(self):
        self.project_id = 1
        self.jocker_id = 1
        

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

    @api.onchange('order_line.project_id')
    def onchange_project_line_e(self):
        lid_project = self.project_id
        #self.order_id = lid_project
        # Trabajando con el entorno del Servidor
        #oc1_id = self.order_id
        #oc1 = self.env['purchase.order'].search([('name', 'like', 'oc1_id')])
        #print(oc1.project_id)
        #oc1.project_id =  lid_project
        #GuiasPurchase_Order._compute_jocker
        raise exceptions.Warning('Proyecto Seleccioando Encabezado: %s' % lid_project.name)
        print("Proyecto Seleccionado: ", self.project_id.name)
        
        return


class GuiasPurchase_OrderLine(models.Model):
    _inherit = 'purchase.order.line'

    active = fields.Boolean('Activo', default=True)
    secuencia_guia = fields.Integer(string="-Secuencia_guia")
    bruto = fields.Float("-Bruto [Lbs]", tracking=True)
    tara = fields.Float("-Tara [Lbs]", tracking=True)
    neto = fields.Float("-Neto [Lbs]", tracking=True)
    # 2021-02-13: 14:25
    contrato = fields.Many2one('maintenance.equipment',string="Equipo Acarreo:", tracking=True, default=1)
    alce = fields.Many2one('maintenance.equipment',string="Equipo CyA:", tracking=True, default=1)
    caja = fields.Many2one('maintenance.equipment',string="Equipo Caja:", tracking=True, default=1)
    project_id = fields.Many2one('project.project',string="Project", default=1)

class BitacoraEstatus(models.Model):
    _name = "guias_pma.estatus"
    _description = "Estatus de Bitacra de Acarrero"

    name = fields.Char('Nombre del Estatus', required=True)
    active = fields.Boolean('Activo', default=True)
    code_estatus = fields.Char('Código de Estatus', required=True)
    description = fields.Text(string='Descripción')
    color_name = fields.Char("Nombre Color")
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('code_estatus_unique',
         'UNIQUE(code_estatus)',
         "El código de Estatus debe ser único"),

        ('name_unique',
         'UNIQUE(name)',
         "El nombre del Esattus debe ser único"),
    ]    


class BitacoraEventos(models.Model):
    _name = "guias_pma.eventos"
    _description = "Eventos de Bitacra de Acarrero"

    name = fields.Char('Nombre del Evento:', required=True)
    active = fields.Boolean('Activo', default=True)
    code_evento = fields.Char('Código de Evento', required=True)
    description = fields.Text(string='Descripción')

    _sql_constraints = [
        ('code_evento_unique',
         'UNIQUE(code_evento)',
         "El código de Evento debe ser único"),

        ('name_unique',
         'UNIQUE(name)',
         "El nombre del Evento debe ser único"),
    ]    

class BitacoraAcarreo(models.Model):
    _name = 'guias_pma.bitacoraacarreo'
    _description = 'Bitacora de Acarreo'
    _check_company_auto = True
    ############################
    name = fields.Char('Nombre Evento', required=False)
    active = fields.Boolean('Activo', default=True)
    code_evento = fields.Many2one('guias_pma.eventos', string='Evento', default=1, trackig=True)
    code_estatus = fields.Many2one('guias_pma.estatus', string='Estatus', default=5, trackig=True)
    description = fields.Text(string='Descripción', trackig=True)
    company_id = fields.Many2one('res.company', store=True, readonly=False, default=lambda self: self.env.company, required=True)
    employee_in_charge = fields.Many2one('hr.employee', string='Empleado', tracking=True)
    frente = fields.Many2one('fincas_pma.frentes', string = 'Frente', tracking=True)
    projects_id = fields.Many2one('project.project',string="Project", default=1, trackig=True)
    contrato = fields.Many2one('maintenance.equipment',string="Equipo:", tracking=True, required=True)
    fechahora = fields.Datetime('Fecha Hora Cosecha', tracking=True,default=fields.Datetime.now)
    fecha = fields.Date('Fecha Cosecha', tracking=True, store=True,default=fields.Datetime.now)
    guia1 = fields.Char('N° Guia 1:', index=True, copy=False, default='0000000000', trackig=True)
    tickete1 = fields.Char('N° Tickete 1:', index=True, copy=False, default='000000', trackig=True)
    guia2 = fields.Char('N° Guia 2:', index=True, copy=False, default='0000000000', trackig=True)
    tickete2 = fields.Char('N° Tickete 2:', index=True, copy=False, default='000000', trackig=True) 
    user_id = fields.Many2one(compute='_compute_user_id', store=True, readonly=False, trackig=True)
        
class BitacoraAca_Col(models.Model):
    _name = 'guias_pma.bitacoraaca_col'
    _description = 'Bitacora de Acarreo por Columna'
    _check_company_auto = True
    ############################
    name = fields.Char('Nombre Evento', required=False)
    active = fields.Boolean('Activo', default=True)
    code_estatus = fields.Many2one('guias_pma.estatus', string='Estatus', default=5, trackig=True)
    description = fields.Text(string='Descripción', trackig=True)
    company_id = fields.Many2one('res.company', store=True, readonly=False, default=lambda self: self.env.company, required=True)
    employee_in_charge = fields.Many2one('hr.employee', string='Empleado', tracking=True)
    frente = fields.Many2one('fincas_pma.frentes', string = 'Frente', tracking=True)
    projects_id = fields.Many2one('project.project',string="Project", default=1, trackig=True)
    contrato = fields.Many2one('maintenance.equipment',string="Equipo:", tracking=True, required=True)
    guia1 = fields.Char('N° Guia 1:', index=True, copy=False, default='0000000000', trackig=True)
    tickete1 = fields.Char('N° Tickete 1:', index=True, copy=False, default='000000', trackig=True)
    guia2 = fields.Char('N° Guia 2:', index=True, copy=False, default='0000000000', trackig=True)
    tickete2 = fields.Char('N° Tickete 2:', index=True, copy=False, default='000000', trackig=True) 
    user_id = fields.Many2one(compute='_compute_user_id', store=True, readonly=False, trackig=True)
    fechahora_sal_fre = fields.Datetime('Fecha Hora Sal. Fre.', tracking=True,default=fields.Datetime.now)
    fechahora_lle_pes = fields.Datetime('Fecha Hora Lle. Pes.', tracking=True,default=fields.Datetime.now)
    fechahora_pesado = fields.Datetime('Fecha Hora Pesado', tracking=True,default=fields.Datetime.now)
    fechahora_des_pat = fields.Datetime('Fecha Hora des. Pat.', tracking=True,default=fields.Datetime.now)
    fechahora_ret_fre = fields.Datetime('Fecha Hora Ret. Fre.', tracking=True,default=fields.Datetime.now)