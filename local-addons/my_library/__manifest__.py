# -*- coding: utf-8 -*-
{
    'name': "my_library",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/library_book.xml',
        'data/data.xml',
        'data/demo.xml',
        'views/library_book_category.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'data/demo.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
    'price': '',
    'currency': 'SGD',
    'sequence': 0,
    'demo': [
        'data/demo.xml',
        ],
}
