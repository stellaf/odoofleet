# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Addon by CLEARCORP S.A. <http://clearcorp.co.cr> and AURIUM TECHNOLOGIES <http://auriumtechnologies.com>
#
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
from odoo import models, fields, api, _

class FleetVehicle(models.Model):

    _inherit = 'fleet.vehicle'

    @api.model
    def create(self, vals):
        acount_obj=self.env['account.analytic.account']
        fleet_id = super(FleetVehicle, self).create(vals)
        account_id=acount_obj.create({'name':self._vehicle_name_get(fleet_id)})
        fleet_id.write({'analytic_account_id':account_id.id,'use_tasks':True,'use_issues':True})
        return fleet_id
     
    def _count_vehicle_task(self):
        project_obj = self.env['project.project']
        self.task_count=len(project_obj.search([('analytic_account_id', '=', self.analytic_account_id.id)]).task_ids)

    def _count_vehicle_issue(self):
        issue_obj = self.env['project.project']
        self.issue_count=len(issue_obj.search([('analytic_account_id', '=', self.analytic_account_id.id)]).issue_ids)

    def _count_swhwlogbook_task(self):
        domain=[('project_id.analytic_account_id', '=', self.analytic_account_id.id), ('task_type_id.name','ilike','SWHW')]
        self.swhw_task_count=self.env['project.task'].search_count(domain)

    def _count_wkshop_task(self):
        domain=[('project_id.analytic_account_id', '=', self.analytic_account_id.id), ('task_type_id.name','ilike','Workshop')]
        self.wkshop_task_count=self.env['project.task'].search_count(domain)
        
    def write(self, vals):
        acount_obj=self.env['account.analytic.account']
        res = super(FleetVehicle, self).write(vals)
        if not self.analytic_account_id:
            account_id=acount_obj.create({'name':self._vehicle_name_get(self)})
            self.write({'analytic_account_id':account_id.id,'use_tasks':True,'use_issues':True})
        self.analytic_account_id.write({'name':self.name,'use_tasks':True,'use_issues':True})
        return res
    
    def _vehicle_name_get(self,record):
        res = record.model_id.brand_id.name + '/' + record.model_id.name + '/' + record.license_plate
        return res

    def action_view_alltasks(self):
        action = self.env.ref('project.act_project_project_2_project_task_all')
        active_id = self.env['project.project'].search([('analytic_account_id', '=', self.analytic_account_id.id)]).id
        context = {'group_by': 'stage_id', 'search_default_project_id': [active_id], 'default_project_id': active_id, }
        return {
            'key2':'tree_but_open',
            'name': action.name,
            'res_model': 'project.task',
            'help': action.help,
            'type': action.type,
            'view_type': action.view_type,
            'view_mode': action.view_mode,
            'res_id': active_id,
            'views': action.views,
            'target': action.target,
            'context':context,
            'nodestroy': True,
            'flags': {'form': {'action_buttons': True}}
        }
	
    def action_view_allissues(self):
        action = self.env.ref('project_issue.act_project_project_2_project_issue_all')
        active_id = self.env['project.project'].search([('analytic_account_id', '=', self.analytic_account_id.id)]).id
        context = {'group_by': 'stage_id', 'search_default_project_id': [active_id], 'default_project_id': active_id,}
        return {
            'name': action.name,
            'res_model': 'project.issue',
            'help': action.help,
            'type': action.type,
            'view_type': action.view_type,
            'view_mode': action.view_mode,
            'views': action.views,
            'target': action.target,
            'res_id': active_id,
            'context':context,
            'nodestroy': True,
            'flags': {'form': {'action_buttons': True}}
        }	
# this part of code, you shall define the project task type to "SWHW" and "Workshop", using the apps in the odoo store, named "task type color"
#    @api.multi
#    def action_view_SWHWlogbooktasks(self):
#        self.ensure_one()
#        action = self.env.ref('project.act_project_project_2_project_task_all')
#        active_id = self.env['project.project'].search([('analytic_account_id', '=', self.analytic_account_id.id)]).id
#        context = {'group_by': 'stage_id', 'search_default_project_id': [active_id], 'default_project_id': active_id,  'task_type_id.name':'SWHW',}
#        return {
#            'key2':'tree_but_open',
#            'name': action.name,
#            'res_model': 'project.task',
#            'help': action.help,
#            'type': action.type,
#            'view_type': action.view_type,
#            'view_mode': action.view_mode,
#            'res_id': active_id,
#            'views': action.views,
#            'target': action.target,
#            'context':context,
#            'nodestroy': True,
#            'flags': {'form': {'action_buttons': True}}
#        }
#
#    @api.multi
#    def action_view_Workshoptasks(self):
#        self.ensure_one()
#        action = self.env.ref('project.act_project_project_2_project_task_all')
#        active_id = self.env['project.project'].search([('analytic_account_id', '=', self.analytic_account_id.id)]).id
#        context = {'group_by': 'stage_id', 'search_default_project_id': [active_id], 'default_project_id': active_id,  'task_type_id.name':'Workshop',}
#        return {
#            'key2':'tree_but_open',
#            'name': action.name,
#            'res_model': 'project.task',
#            'help': action.help,
#            'type': action.type,
#            'view_type': action.view_type,
#            'view_mode': action.view_mode,
#            'res_id': active_id,
#            'views': action.views,
#            'target': action.target,
#            'context':context,
#            'nodestroy': True,
#            'flags': {'form': {'action_buttons': True}}
#        }

    analytic_account_id = fields.Many2one('account.analytic.account',string='Analytic Account')
    task_count = fields.Integer(compute=_count_vehicle_task, string="Vehicle Tasks" , multi=True)
    issue_count = fields.Integer(compute=_count_vehicle_issue, string="Vehicle Issues" , multi=True)
#    swhw_task_count = fields.Integer(compute=_count_swhwlogbook_task, string="SWHWlogbook Tasks" , multi=True)
#    wkshop_task_count = fields.Integer(compute=_count_wkshop_task, string="workshop Tasks" , multi=True)
 
    
class  fleet_vehicle_log_services(models.Model):

    _inherit = 'fleet.vehicle.log.services'
    invoice_id = fields.Many2one('account.invoice',string='Facture')
 
