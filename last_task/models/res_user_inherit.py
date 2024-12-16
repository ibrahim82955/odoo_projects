from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    # res_user_phone = fields.Char(related='partner_id.phone', string='phone',readonly=True)
    national_idd = fields.Char(related='parent_id.national_id')

