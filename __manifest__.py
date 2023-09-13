# -*- coding: utf-8 -*-
{
    'name': "gse_employee",

    'summary': """
        Customizations pour Goshop Energy""",

    'description': """
    """,

    'author': "Sébastien Bühl",
    'website': "http://www.buhl.be",

    'category': 'Customizations',
    'version': '0.1.8.6',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr',
        'hr_appraisal',
        'hr_holidays',
    ],

    'data': [
        'views/view.xml',
        
    ],
    'assets': {
        
    },
}
