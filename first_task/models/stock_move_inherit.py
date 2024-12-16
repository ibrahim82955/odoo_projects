# -*- coding: utf-8 -*-

from odoo import models, fields, api


class stock_move_inherit(models.Model):
    _inherit='stock.move'
    
    
    # this field help my to acces the fields in sale.order.line
    sale_line_id = fields.Many2one(comodel_name='sale.order.line') 
    stock_move_inherit_dimention  = fields.Char('dimention',store=True ,related='sale_line_id.sale_order_line_dimension')
    
    
    # def write(self,vals):
    #         vals['stock_move_inherit_dimention']=self.sale_line_id.sale_order_line_dimension
    #         return super(stock_move_inherit,self).write(vals)
    
    

    
