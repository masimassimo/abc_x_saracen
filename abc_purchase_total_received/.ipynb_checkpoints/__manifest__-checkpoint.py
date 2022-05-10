# -*- coding: utf-8 -*-
{
    'name': "ABC Calculate amount from received quantity",

    'summary': """
        Change total amount computation on purchase orders""",

    'description': """
        The total amount of the purchase order and lines will be calculated from received quantity""",

    'author': "Masi Massimo",
    'website': "https://www.abcstrategie.it,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchase',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
