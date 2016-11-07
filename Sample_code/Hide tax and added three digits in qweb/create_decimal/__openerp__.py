{
    'name': 'Create Decimal',
    'version': '0.1',
    'sequence': 1,
    'summary': 'Create Decimal Details',   
    'website': 'http://ifensys.com/', 
    'description': 'Create Decimal Details.',
    'author': 'Brand Equity Solutions',
    'depends' : ['base', 'sale','purchase', 'account', 'account_accountant'],  
    'data' : [
              
              'views/reports/inherited_sale_report_templates.xml',
              'views/reports/inherited_purchase_order_templates.xml',
                        
    ],
    'qweb' : ["static/src/xml/*.xml"],
    'demo' : [],
    'test' : [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'bootstrap': True,
}