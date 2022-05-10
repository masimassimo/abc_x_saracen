# -*- coding: utf-8 -*-
{
    'name': "Invia copia RFQ",

    'summary': """
        Questo modulo invia una copia della RFQ ad un indirizzo email prestabilito""",

    'description': """
        Questo modulo invia una copia della RFQ ad un indirizzo email prestabilito
    """,

    'author': "Massimo Masi",
    'website': "https://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/purchase_order_calculated.xml',
        'report/purchase_reports.xml',
        'data/mail_template_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
