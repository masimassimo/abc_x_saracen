# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_stock_move",

    'summary': """
        ABC Q.tà Completata sul movimento d'origine""",

    'description': """
        ABC Q.tà Completata sul movimento d'origine
    """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it",
    
    'category': 'Stock',
    'version': '0.1',

    'depends': ['base','stock'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'demo': [],
}
