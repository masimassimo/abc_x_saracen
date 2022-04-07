# -*- coding: utf-8 -*-
# QUESTO MODULO PERMETTE DI VISUALIZZARE SULLA RIGA DI UN MOVIMENTO DI MAGAZZINO
# LA QUANTITA COMPLETATA NELL'ORDINE DI ORIGINE IN MODO
# ANCHE SE E' SUPERIORE A QUELLA RICHIESTA
{
    'name': "ABC Q.tà Completata sul movimento d'origine",

    'summary': """
        ABC Q.tà Completata sul movimento d'origine""",

    'description': """
        ABC Q.tà Completata sul movimento d'origine
    """,

    'author': "Massimo Masi",
    'website': "https://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
