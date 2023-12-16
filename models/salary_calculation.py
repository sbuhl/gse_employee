from odoo import models, fields, api
from time import time

class SalaryCalculation(models.TransientModel):
    _name = 'salary.calculation.wizard'
    _description = 'Salary Calculation Wizard'

    net_salary = fields.Float('Net Salary (USD)')
    basic_salary = fields.Float('Basic Salary (USD)')
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
    ], string='Month') 

    structure_type_id = fields.Many2one('hr.payroll.structure.type', string="Salary Structure Type")

    tolerance_threshold = fields.Float('Tolerance Threshold')

    def calculate_salary(self):
        if self.structure_type_id.name == 'Employee':
            self.basic_salary = 0.5 * self.net_salary
        elif self.structure_type_id.name == 'Worker':
            self.basic_salary = 0.7 * self.net_salary 
        return {
            'name': 'Salary Calculation',
            'type': 'ir.actions.act_window',
            'res_model': 'salary.calculation.wizard',
            'res_id': self.id,
            'view_mode': 'form',
            'view_id': self.env.ref('gse_employee.view_salary_calculation_wizard_form').id,
            'view_type': 'form',
            'target': 'new',
        }
    
    # def calculate_basic_salary(net_salary, salary_structure, max_iterations, max_iteration_time):
    #     basic_salary = net_salary / 2.0
    #     threshold = 0.01 
        
    #     start_time = time.time()

    #     for iteration in range(max_iterations):
    #         end_time = time.time()
    #         elapsed_time = end_time - start_time

    #         if elapsed_time > max_iteration_time:
    #             break

    #     return basic_salary

