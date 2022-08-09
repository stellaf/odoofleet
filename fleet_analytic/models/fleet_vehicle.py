# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api, _


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    analytic_account_id = fields.Many2one(comodel_name='account.analytic.account', string='Analytic Account')

    @api.model
    def create(self, vals):
        
        _logger.warning(f'{self} {vals}')
        if vals.get('license_plate') and not vals.get('analytic_account_id',False):
            analytic = self.env['account.analytic.account'].search([('name','=',vals.get('license_plate'))],limit=1)
            if not analytic:
                analytic = self.env['account.analytic.account'].create({'name':vals.get('license_plate')})
            vals['analytic_account_id'] = analytic.id
        return super(FleetVehicle, self).create(vals)
     
    def write(self, vals):
        for vehicle in self:
            _logger.warning(f'write {vals.get("license_plate")} anaöytic {vals.get("analytic_account_id",False)}')
            if vals.get('license_plate') and not vals.get('analytic_account_id',False):
                _logger.warning(f'write {self} {vals}')
                analytic = self.env['account.analytic.account'].search([('name','=',vals.get('license_plate'))],limit=1)
                if not analytic:
                    analytic = self.env['account.analytic.account'].create({'name':vals.get('license_plate')})
                vals['analytic_account_id'] = analytic.id
            super(FleetVehicle, self).write(vals)
