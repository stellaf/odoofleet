# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2023- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Fleet: Biluppgifter',
    'version': '14.0.0.0.0',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'The Fleet Biluppgifter module automates vehicle  information retrieval from biluppgifter.se, improving accuracy and efficiency in fleet management with registration numbers.',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'description': """
    The Fleet Biluppgifter module is an add-on to the Fleet module that makes it easy to fill in vehicle information. By entering the vehicles registration number, the module searches for and retrieves all available information about the vehicle from biluppgifter.se, a Swedish website. This information is then automatically populated into the relevant fields, making it quick and easy to update vehicle information. With the Fleet Biluppgifter module, you can ensure that all vehicle data is accurate and up-to-date, saving you time and improving the efficiency of your fleet management.
    """,
    #'sequence': '1',
    'author': 'Salih Marwan',
    'website': 'https://vertel.se/apps/',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-',
    'depends': ['base', 'fleet'],
    'data': [
        'views/fleet_vehicle_view.xml'       
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
    # Any module necessary for this one to work correctly
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
