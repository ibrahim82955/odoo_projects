
from odoo import models, fields, api

class thirdtask(models.Model):
    _inherit = 'res.partner'

    allowed_discount = fields.Float(string='"allowed discount')
    

