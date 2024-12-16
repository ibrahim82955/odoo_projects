# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_temp_dimenstion(models.Model):
    _inherit='product.template'
    
    
    
    product_temp_dimenstion_dimension  = fields.Char(string='dimension')

    
