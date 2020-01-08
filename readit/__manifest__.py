# -*- coding: utf-8 -*-
{
    'name': "Readit",
    'summary': "A company forum where any topic can be discussed.",
    'description': "",

    'author': "Odoo",
    'website': "http://www.odoo.com",

    'application': True,
    'installable': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'license': 'AGPL-3',
    'category': 'Readit',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['contacts', 'renderlistcontent'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ]
}
