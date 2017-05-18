# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Accounting Charts Customization',
    'version': '1.1',
    'depends': ['base', 'product'],
    'sequence': 13,
    'data': [
        'stock_move_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
