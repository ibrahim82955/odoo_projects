from odoo import _, api, fields, models, tools
class saleorder (models.Model):
    _inherit='sale.order'
    
    
    
    technicalorde_id=fields.Many2one('technical_order.orders',string='technical_id',readonly=True)
    
    
    total_price  = fields.Float(string='total price')
    
    
    
    
    
    
    # @api.onchange('order_line')
    # def quantity_contrains(self):
    #         hemooo = self.technicalorde_id.OrderLine_ids
    #         for rec in hemooo:
    #             for record in self.order_line:
    #                 if rec.product_id.id == record.product_id.id :
                
                
                
                
            
            
             
            # if self.product_uom_qty > hemooo:
            #     raise ValidationError("quantity is incorrect")
            
            # self.env['technical_order.line'].quantity=self.env['technical_order.line'].quantity-self.product_uom_qty
            
            # for line in self:
            #     if line.product_uom_qty > self.env['technical_order.line'].quantity:
            #         raise ValidationError(_("Quantity exceeds the maximum allowed quantity for this product."))
                
