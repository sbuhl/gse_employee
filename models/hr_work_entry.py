# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models


class HrWorkEntry(models.Model):
    _name = 'hr.work.entry'
    _inherit = 'hr.work.entry'
    
    salary_work_structure_id = fields.Integer(
        string="Structure Type",
        related='contract_id.structure_type_id.id',
        store=True,  
        readonly=True 
    )

    contract_id = fields.Many2one('hr.contract')
