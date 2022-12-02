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
    fechahora_lle_pes = fields.Datetime('Fecha Hora Lle. Pes.', tracking=True)
    fechahora_pesado = fields.Datetime('Fecha Hora Pesado', tracking=True)
    fechahora_des_pat = fields.Datetime('Fecha Hora des. Pat.', tracking=True)
    fechahora_ret_fre = fields.Datetime('Fecha Hora Ret. Fre.', tracking=True)