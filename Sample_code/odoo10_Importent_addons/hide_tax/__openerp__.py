{
    'name' : 'Tax Disable',
    'version' : '1.0',
    'author' : 'Ifensys',
    'description': """
        This module customizes default behaviour of tax configuration on 
        sale order's, purchase order's and Invoices, And also hiding the tax 
        menu from the Accounting configuration menu
    """,
    'category': 'Accounts and Tax Configuration',
    'website' : 'www.ifensys.com',
    'depends' : ['create_decimal'],
    'images': ['images/main_screenshot.png'],
    'demo' : [],
    'data' : [
            'views/sale_view.xml',
            'views/product_view.xml',
            'views/account_view.xml',
            'views/purchase_view.xml',
            'views/custom_header_report.xml',
            'data/paper_format.xml'
            ],
    'test' : [],
    'auto_install': False,
    'application': True,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
