# -*- coding: utf-8 -*-
{
    'name': "website_social",

    'summary': """
        Extension for add more Social Networks to Odoo""",

    'description': """
        Extension for add more Social Networks to Odoo Website, like Bitbucket, Instagram, Vimeo, Whatsapp, Twitch, Reddit, etc.
    """,

    'author': "Moldeo Interactive",
    'website': "https://www.moldeointeractive.com.ar",

    'category': 'Website',
    'version': '10.0',

    'depends': ['base', 'website', 'website_sale'],

    'data': [
        'views/views.xml',
    ],
    'demo': [
    ],
}
