# -*- coding: utf-8 -*-
{
    'name': "Modificated Point of Sale",
    'description': """
        Answers of Tests Technical for module Point of Sale
    """,

    'author': "Jean Espinoza",
    'website': "https://portafolio.jespinoza.site/",
    'category': 'Point of Sale',
    'version': '0.1',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/answer_one.xml',
    ],
    'demo': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'point_of_sale_modificated/static/src/js/answer_two.js',
            'point_of_sale_modificated/static/src/xml/answer_three.xml',  
            'point_of_sale_modificated/static/src/js/answer_three.js'
        ],
    },
    'installable': True,
    'application': True,
}
