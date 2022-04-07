# -*- coding: utf-8 -*-
# QUESTO MODULO AGGIUNGE ALL'APP BARCODE UN CAMPO PER SPECIFICARE LA DATA DI SCADENZA DEL LOTTO DURANTE LA RICEZIONE
{
    'name': "ABC Scadenza Lotto ricezione con Barcode",

    'summary': """
        Questo modulo aggiunge la possibilità di specificare la Data di scadenza del lotto durante la ricezione merce, con l'app Barcode""",

    'description': """
        Questo modulo aggiunge la possibilità di specificare la Data di scadenza del lotto durante la ricezione merce, con l'app Barcode
    """,

    'author': "Massimo Masi",
    'website': "https://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','barcodes','stock_barcode'],

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
