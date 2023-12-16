# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _ 


class Contract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Contract Form extension'

    net_salary = fields.Monetary('Net Salary (USD)')
    month = fields.Selection([
        ('january', 'January'),
        ('february', 'February'),
        ('march', 'March'),
        ('april', 'April'),
        ('may', 'May'),
        ('june', 'June'),
        ('july', 'July'),
        ('august', 'August'),
        ('september', 'September'),
        ('october', 'October'),
        ('november', 'November'),
        ('december', 'December'),
    ], string='Month', required=True)
    tolerance_threshold = fields.Float('Tolerance Threshold')

    def open_salary_calculation_wizard(self): 
        wizard = self.env['salary.calculation.wizard'].create({}) 
        return {
            'name': 'Salary Calculation',
            'type': 'ir.actions.act_window',
            'res_model': 'salary.calculation.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('gse_employee.view_salary_calculation_wizard_form').id,
            'target': 'new', 
        }