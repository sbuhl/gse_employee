# -*- coding: utf-8 -*-

from odoo import fields, models

class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'
    
    struc_type = fields.Char(related="employee_id.contract_id.structure_type_id.name", string='Salary Structure', store=True)
    work_location = fields.Char(related="employee_id.work_location_id.display_name", string='Work Location', store=True)

class HolidaysAllocation(models.Model):
    _inherit = "hr.leave.allocation"
    
    struc_type = fields.Char(related="employee_id.contract_id.structure_type_id.name", string='Salary Structure', store=True)
    work_location = fields.Char(related="employee_id.work_location_id.display_name", string='Work Location', store=True)
