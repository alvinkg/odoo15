# -*- coding: utf-8 -*-
{
    'name': "my_library",

    'summary': """
        Library in Odoo
        """,

    'description': """
        Library in Odoo
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'mail','website'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        # 'data/data.xml',
        # 'data/demo.xml',
        'data/library_stage.xml',
        'views/views.xml',
        # 'views/templates.xml',
        'views/library_book.xml',
        'views/library_book_rent.xml',        
        'views/library_book_category.xml',
        'wizard/library_book_rent_wizard.xml',
        'wizard/library_book_return_wizard.xml',
        'reports/book_rent_report.xml',
        'reports/book_rents_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [          
            'my_library/static/src/scss/my_library.scss',
            'my_library/static/src/css/my_library.css',
            'my_library/static/src/js/my_library.js',
            ],
        'web.assets_backend': [          
            'my_library/static/src/js/component.js',
            ],
    },
    'application': True,
    'license': 'LGPL-3',
    'price': '',
    'currency': 'SGD',
    'sequence': 0,
    # only loaded in demonstration mode
    'demo': [
        'data/demo.xml',
        ],
    'post_init_hook': 'add_book_hook',
}
