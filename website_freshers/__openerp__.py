{
    'name': 'Web Freshers',
    'category': 'Website',
    'version': '1.0',
    'summary': 'List all freshers in web form',
    'description': """
                    Odoo Freshers Form
                    ====================
            """,
    'author': 'George Vincent',
    'depends': ['base','website_partner', 'website_mail','hr_recruitment'],
    'data': [
        'data/config_data.xml',
        'views/freshers_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
}
