# -*- coding: utf-8 -*-
{
    'name': "Account Modificated",
    'description': """
        Answers of Tests Technical for module Account
    """,

    'author': "Jean Espinoza",
    'website': "https://portafolio.jespinoza.site/",
    'category': 'Accounting/Accounting',
    'version': '0.1',
    'depends': ['base', 'account','stock','point_of_sale'],
    'data': [
        'views/answer_four.xml',
        'views/answer_six.xml',
        'views/answer_seven.xml',
        'views/answer_eigth.xml',
        'security/ir.model.access.csv',
        'data/data_sales_channel.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
}

