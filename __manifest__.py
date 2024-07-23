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
    'version': '17.0.0.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr',
        'hr_appraisal',
        'hr_contract',
        'hr_holidays',
        'hr_skills',
        'hr_work_entry',
    ],

    'data': [
        'views/view.xml',
        'views/work_entry.xml',
        'views/res_users.xml',
    ],
    'assets': {
        
    },
}
