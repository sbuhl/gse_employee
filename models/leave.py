# -*- coding: utf-8 -*-

from odoo import fields, models

class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'
    
    struc_type = fields.Char(related="employee_id.category_ids.display_name", string='Salary Structure')
