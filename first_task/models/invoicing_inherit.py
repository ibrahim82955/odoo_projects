# -*- coding: utf-8 -*-

from odoo import models, fields, api


class invoicing_inherit(models.Model):
    
    _inherit = 'account.move.line'
    

    hema_dimension_inherit = fields.Char(string='Dimension',readonly=True)


    

    

    

    
