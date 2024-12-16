# -*- coding: utf-8 -*-

from odoo import models, fields, api


class invoicing_inherit(models.Model):
    
    _inherit = 'account.move.line'
    
    discountt_inherit = fields.Float(string='discount',readonly=True)
    



    

    

    

    
