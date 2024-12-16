from odoo import models, fields, api,_
from odoo.exceptions import ValidationError, UserError
class productt(models.Model):
    _inherit='product.product'
    







class technical_order_quntity(models.Model):
    _inherit = 'sale.order.line'
    hemooo  =  fields.Float()
    # remining_quantity  =   fields.Float()
    
    
    

    # @api.depends('product_uom_qty')
    # def quantity_contrains(self):
    #         hemooo = self.env['technical_order.line'].quantity
    #         if self.product_uom_qty > hemooo:
    #             raise ValidationError("quantity is incorrect")
            
    #         self.env['technical_order.line'].quantity=self.env['technical_order.line'].quantity-self.product_uom_qty
            
    #         for line in self:
    #             if line.product_uom_qty > self.env['technical_order.line'].quantity:
    #                 raise ValidationError(_("Quantity exceeds the maximum allowed quantity for this product."))
            
    # @api.onchange('product_uom_qty')
    # def update_hemooo(self):
    #     for line in self:
    #         if line.product_uom_qty > line.order_id.OrderLine_ids.filtered(
    #             lambda order_line: order_line.product_id.id == line.product_id.id
    #         )
    #             raise ValidationError('Product quantity cannot exceed the Technical Order quantity.')
            
            
    #     active_id = self.env.context.get('active_id')
    #     if active_id:
    #         technical = self.env['technical_order.line'].browse(active_id)
    #         technical.write({
    #             'remining_quantity_order':self.hemooo
    #         })    
            
            
            
            

            
        

    

