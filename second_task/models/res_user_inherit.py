from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    national_id = fields.Integer(related='partner_id.national_id', string='national id',readonly=True)
    
