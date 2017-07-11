# -*- coding: utf-8 -*-
{
    'name': "Merced 1.0",

    'summary': """
        Generador de codigo de barras,
        Impresion de etiqueta con la clasificación y
        Agrega un campo a res.partner""",

    'description': """
        Modulo creado para Fundación Merced
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'views/add_field_view.xml',
        'views/generador_view.xml',
        'views/classification_view.xml',
        'views/list_view.xml',
        'report/report_product_labels.xml',
        'views/ref_internal.xml',
    ],
    'qweb': ['static/src/xml/ref_internal.xml'],
    'js': ['static/src/js/*.js'],
    'installable':True,
    'auto_install':False,
}