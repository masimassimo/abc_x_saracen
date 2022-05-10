# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_card_manager",

    'summary': """
        Modulo per gestire le carte associate al cliente.""",

    'description': """
        Modulo per gestire le carte associate al cliente.
    """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Contacts',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/card_manager.xml',

    ],    
    "installable": True,
    "application": True,
    'demo': [],
}