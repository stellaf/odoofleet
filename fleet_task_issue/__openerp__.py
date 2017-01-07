# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Addon by stella.fredo@gmail.com based on 
#    fleet_analytic_account app from CLEARCORP S.A. (<http://clearcorp.co.cr>).
#    AURIUM TCHNOLOGIES (<http://auriumtechnologies.com>).
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : 'Fleet Task Issue',
    "version" : '1.0',
    "author" : 'stella.fredo@gmail.com',
    'complexity': 'normal',
    "description":  """
Fleet - Task Issues
=============================
This module link the fleet and project with one analytic account. 
when you create one vehicle
-------------
		* one project with the same vehicle name will be created under the project menu.
		* thus you can schedule the task and issues for this vehicle.
		* smart buttons to this vehicles task and issues will be added to each vehicle's form.
    """,
    "category": 'Managing vehicles tasks and issues',
    "sequence": 3,
    "website" : "https://github.com/stellaf/odoofleet.git#8.0",
    "images" : [],
    "depends" : [
                 'fleet',
                 'account_analytic_analysis',
		 'account',
		 'project',
                 'project_issue'
                 ],
    "data" : ['fleet_task_issue_view.xml'],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [],
    "test" : [],
    "auto_install": False,
    "application": False,
    "installable": True,
    'license': 'AGPL-3',
}
