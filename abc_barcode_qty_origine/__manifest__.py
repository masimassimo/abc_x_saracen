# -*- coding: utf-8 -*-
# QUESTO MODULO PERMETTE DI VISUALIZZARE NELL'APP BARCODE LA QUANTITA DEL MOVIMENTO DI MAGAZZINO DI ORIGINE
# CALCOLATA DAL MODULO ABC_STOCK_MOVE
{
    'name': "Quantità movimento di origine nell'app Barcode",

    'summary': """
        Quantità movimento di origine nell'app Barcode""",

    'description': """
        Modulo ponte per visualizzare la quantità del movimento di magazzino di origine nell'app barcode
    """,

    'author': "Massimo Masi",
    'website': "https://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','abc_barcode_scadenza','abc_stock_move'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    'qweb': [
        'static/src/xml/extend_barcode.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
