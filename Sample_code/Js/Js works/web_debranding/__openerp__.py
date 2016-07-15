{
    'name': 'Debranding',
    'category': 'Hidden',
    'version': '1.0',
    'description':'Debranding',
    'depends': ['base', 'web'],
    'auto_install': True,
    'data': [
        'views/webclient_templates.xml',
    ],
    'qweb' : [
        "static/src/xml/*.xml",
    ],
    'bootstrap': True, # load translations for login screen
}
