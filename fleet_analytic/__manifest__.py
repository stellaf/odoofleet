# -*- coding: utf-8 -*-
{
    'name': 'Fleet: Analytic',
    'category': 'Accounting',
    'summary': 'Fleet bridge. Manage analytic accounting with fleets',
    'description': "",
    'version': '1.0',
    'depends': ['fleet', 'account'],
    'data': [
        'views/fleet_vehicle_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
    'license': 'LGPL-3',
}
