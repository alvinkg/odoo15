# -*- coding: utf-8 -*-
{
    'name': "POS demo",
    'summary': "Point of sale demo module",
    'description': """Point of sale demo module""",
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Point of Sale',
    'version': '15.0.1',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_assets.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            "pos_demo/static/src/js/pos_demo.js",
            "pos_demo/static/src/scss/pos_demo.scss",
            ],
    },
    'application': True,
    'license': 'LGPL-3',
    'price': '1',
    'currency': 'SGD',
    'sequence': 1,
}
