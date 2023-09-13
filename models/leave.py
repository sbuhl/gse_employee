# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'
    
    struc_type = fields.Char(related="employee_id.contract_id.structure_type_id.name", string='Salary Structure', store=True)
    work_location = fields.Char(related="employee_id.work_location_id.display_name", string='Work Location', store=True)

class HolidaysAllocation(models.Model):
    _inherit = 'hr.leave.allocation'
    
    struc_type = fields.Char(related="employee_id.contract_id.structure_type_id.name", string='Salary Structure', store=True)
    work_location = fields.Char(related="employee_id.work_location_id.display_name", string='Work Location', store=True)

class Employee(models.Model):
    _inherit = 'hr.employee'

    goal_count = fields.Integer(compute='_compute_goal_count', string="Goal Count")
    goaly_ids = fields.One2many('hr.appraisal.goal', 'employee_id', string="Goals")
    
    duties = fields.Html(string="Duties")

    @api.depends('goaly_ids')
    def _compute_goal_count(self):
        for record in self:
            record.goal_count = len(record.goaly_ids)
    
    def action_view_goals(self):
        return {
            'name': _('Goals'),
            'res_model': 'hr.appraisal.goal',
            'view_mode': 'list,form',
            'context': {
                'search_default_employee_id': self.id,
            },
            'target': 'current',
            'type': 'ir.actions.act_window',
        }

class HrEmployeePublic(models.Model):
    _inherit = "hr.employee.public"

    duties = fields.Html(readonly=True)
    goaly_ids = fields.One2many('hr.appraisal.goal', 'employee_id', string="Goals", readonly = True)
    
