# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sale_order_line_dimension(models.Model):
    _inherit='sale.order.line'
    
    
    
    sale_order_line_dimension = fields.Char(string='dimension',related='product_template_id.product_temp_dimenstion_dimension',readonly=False) 

    hemas_ids = fields.One2many(comodel_name='stock.move',inverse_name='sale_line_id')
    
    def _prepare_invoice_line(self,**optional_values):
        res = super()._prepare_invoice_line(**optional_values)
        print('dgfdfgdgf',res)
        res['hema_dimension_inherit'] = self.hemas_ids.stock_move_inherit_dimention
        print('after',res)

        return res
    
    # def _prepare_procurement_values(self, group_id=False):
    #     res = super(sale_order_line_dimension, self)._prepare_procurement_values(group_id)
    #     res.update({'stock_move_inherit_dimention': self.sale_order_line_dimension})
    #     return res
    
    

    

