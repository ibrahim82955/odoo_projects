from odoo import models, fields, api,_

class partener_add(models.Model):
    _inherit='res.partner'
    
    set_the_value   = fields.Boolean()