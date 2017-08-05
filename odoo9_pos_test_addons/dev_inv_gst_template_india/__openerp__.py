# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd. (<http://www.devintellecs.com>).
#
##############################################################################


{
    'name': 'Indian GST Invoice Format',
    'version': '1.0',
    'sequence':1,
    'category': 'Account',
    'description': """
        App will print New Invocie Format of Indian GST.
    """,
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'summary': 'App will print New Invocie Format of Indian GST.',
    'website': 'http://www.devintellecs.com/',
    'images': ['images/main_screenshot.jpg'],
    'depends': ['account'],
    'data': [
        
        'dev_gst_invoice_menu.xml',
        'report/demo_gst_invoice_report.xml',
        'view/res_partner.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

