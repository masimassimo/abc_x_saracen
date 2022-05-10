# -*- coding: utf-8 -*-
{
    'name': "Report di Stampa Ordini di Acquisto Senza Prezzi",

    'summary': """
        Report di Stampa Ordini di Acquisto Senza Prezzi""",

    'description': """
        Report di Stampa Ordini di Acquisto Senza Prezzi
    """,

    'author': "Massimo Masi",
    'website': "https://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchases',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/purchase_order_wo_prices.xml',
        'report/purchase_reports.xml',
        'report/purchasequotation_ext.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
