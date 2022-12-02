# -*- coding: utf-8 -*-
{
    'name': "guias_pma",

    'summary': """
        Adecuación de fincas para Panamá y módulos de compras y ventas para
        almnacenar dos datos de las guias de cañas de un ingenio de azúcar""",

    'description': """
        Herencia en los modelos y vistas de.
        - compras (compra de caña)
        - ventas (venta de servicio de gestion de fincas)
        Para ver la información que proviene de las.
        - 2021-02-13: Agregar campo proyecto_id al modelo: purchase_line y las vistas relacionadas.
                    - Campos: project_id, caja, alce y contrato.
        - 2021-02-19: Pantalla de Bitacora de Acarreo.
        - 2021-02-26: Agregando valores por default a: project_id, caja, alce y contrato.
        - 2021-03-08: Agregando al Menu Formulario: Bitácora de Logistica o Estatus de Equipo de Acarreo.
        - 2021-03-09: Agregando Maestro de Estatus y Eventos a la Bitacora de Eventos de Acarreo.
        - 2021-03-16: Agrenfo otra Bitacora por Columna
    """,

    'author': "Alconsoft",
    'website': "http://www.alconsoft.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2021-03-16 - 14:45',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'fincas_pma'],

    # always loaded: Aqui se cargan los formularios de vista.
    # IMPORTANTE: SE QUITA EL CARACTER "#" PARA QUE SE PUEDA CARGAR ARCHIVO CON LA LISTA DE ACCESO DE SEGURIDAD
    'data': [
        ####### ESTO IMPEDIA QUE SE PUDIERA VER EL MENU ########################
        ###############################
        'security/bitacora_security.xml',
        'security/ir.model.access.csv',
        'views/compras_views.xml',
        'views/bitacora_acarreo.xml',
        #'views/templates.xml',
        ####### CARGA AUTOMATICA AL INSTALAR DE DATOS ESTATICOS ########################
        'static/xls/product.template.csv',
        'static/xls/guias_pma.estatus.csv',
        'static/xls/guias_pma.eventos.csv',
        ###############################
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Aplicacion:  si aparace cierto (true) esta modulo sera una aplicacion que aprecera en el listado de aplicaciones de odoo.
    'application': True,
}
