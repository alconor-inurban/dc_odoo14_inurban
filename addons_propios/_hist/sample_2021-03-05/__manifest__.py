# -*- coding: utf-8 -*-
{
    'name': "sample",

    'summary': """
        Strange Matter: Materia Extraña en mestras de Caña de Azúcar""",

    'description': """
        Strange Matter: Materia Extraña en mestras de Caña de Azúcar.
        - Se agregó alertas amarilla y roja a los items (contenido de M.E. materia Extraña)
        - Se cambió archivo de configuracón de sample (Muestras).
        - Se agregaron las alertas generales de la muestra para Caña larga, En Tiempo y % de Muestra.
        - 2021-02-02 - Se agregó campo "longitud_Avg1" en el encabezado, para no usar el campo: longitud_Avg en elñ detalle
        - 2021-02-13 - Diatraea
        - 2021-02-19 - Duración
    
    """,

    'author': "Alconsoft",
    'website': "http://www.alconsoft.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': 'Rama main 2021-02-19 - 16:20',

    # any module necessary for this one to work correctly
    # 'report',
    'depends': ['base','purchase','fincas_pma', 'guias_pma'],

    # always loaded
    'data': [
        'security/sample_security.xml',
        'security/ir.model.access.csv',
        'views/sample_views.xml',
        'views/sample_config_views.xml',
        'views/templates.xml',
        'data/sample_data.xml',
        'static/xls/product.category.csv',        
        'static/xls/product.template.csv',
        'report/sample_reports.xml',
        'report/purchase_report_views.xml',
        #'report/purchase_order_templates.xml',
        #'report/purchase_quotation_templates.xml',
        #'report/purchase_bill_views.xml',        
    ],
    #'qweb': [
    #"static/src/xml/purchase_dashboard.xml",
    #"static/src/xml/purchase_toaster_button.xml",
    #],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
