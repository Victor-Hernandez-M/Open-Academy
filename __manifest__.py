# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        
        Este modulo fue desarrollado como un proyecto para la clase de industria del software, basandose en la documentacion proporcionada por odoo""",

    'description': """
        Modulo de open academy creado para la clase de industria del software
    """,

    'author': "Victor Hernandez",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
