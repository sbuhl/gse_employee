# -*- coding: utf-8 -*-
from odoo import fields, models

class ResUsers(models.Model):
    _inherit = "res.users"

    job_id = fields.Many2one('hr.job', compute='_compute_job_id',
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", string='Employee Job Position')

    def _compute_job_id(self):
        for user in self:
            if user.employee_ids:
                # Handling multiple employee records by taking the first one
                user.job_id = user.employee_ids[0].job_id if user.employee_ids[0].job_id else False
            else:
                # In case there are no employee records
                user.job_id = False
