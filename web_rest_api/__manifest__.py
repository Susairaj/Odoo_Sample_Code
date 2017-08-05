{
    'name': 'Rest API',
    'author': 'Boscosoft',
    'version': '1.0',
    'category': 'API',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'views/res_user_views.xml',
        'views/rest_api_access_history_views.xml',
        'views/expire_token_cron.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
