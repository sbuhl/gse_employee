# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _ 


class Contract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Contract Form extension'

    def open_salary_calculation_wizard(self): 
        wizard = self.env['salary.calculation.wizard'].create({
            # 'employee_id': self.employee_id.id,
            # 'contract_id': self.id,
        #     'date_from': self.date_start,
        #     'date_to': self.date_end,
        }) 
        
        

        return {
            'name': 'Salary Calculation',
            'type': 'ir.actions.act_window',
            'res_model': 'salary.calculation.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('gse_employee.view_salary_calculation_wizard_form').id,
            'target': 'new', 
        }