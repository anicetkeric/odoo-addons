# -*- encoding: utf-8 -*-
{
    'name': 'HR Mission',
    'description': """
Use to manage employee mission outside company.
=================================================================================================
""",
    'author': 'Boanergues',
    'version': '0.1',
    'depends': ['base', 'hr', 'account_accountant', 'report', 'calendar', 'resource'],
    'category': 'Human Resources',
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/hr_mission_view.xml',
        'views/expense_view.xml',
        'reports/reports.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
