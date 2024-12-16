from odoo import fields, models


class Respartner(models.Model):
    _inherit = 'res.partner'
    national_id= fields.Integer()

