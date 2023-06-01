# -*- coding: utf-8 -*-

from odoo import fields, models

class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'
    
    struc_type = fields.Char(related="employee_id.contract_id.structure_type_id.name", string='Salary Structure', store=True)

