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
        'hr_contract',
        'hr_holidays',
        'hr_skills',
        'hr_work_entry',
        'hr_payroll',
    ],

    'data': [
        'views/view.xml',
        'views/work_entry.xml',
        'views/hr_contract_views.xml',
        'views/salary_calculation_wizard.xml',
        'security/ir.model.access.csv'
    ],
    'assets': {
        
    },
}
