# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ventor Base',
    'version': '12.0.1.2.1',
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'license': 'LGPL-3',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'summary': 'Base module that allow relation between Ventor modules',
    'depends': [
        'base',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config.xml',
        'views/res_users.xml',
        'views/stock_picking.xml',
    ],
    'post_init_hook': '_auto_fill_settings',
}
