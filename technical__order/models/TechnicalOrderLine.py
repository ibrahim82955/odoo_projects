
from odoo import _, api, fields, models, tools



class TechnicalOrderLine(models.Model):
    _name = 'technical_order.line'
    _description = 'Technical Order Line'

    id=fields.Integer()
    product_id = fields.Many2one('product.product', string='Product', required=True)
    description = fields.Char(string='Description', related='product_id.name', readonly=True)
    quantity = fields.Float(string='Quantity', default=1)
    price = fields.Float(string='Price', related='product_id.list_price', readonly=True)
    total = fields.Float(string='Total', compute='_compute_total', readonly=True)
    order_id = fields.Many2one(comodel_name="technical_order.orders", string="order_id",readonly=True ,required=False )
    remining_order=fields.Float(readonly=True,store=True)
    order_quantity=fields.Float(store=True) #amount of the product customer want to use to make so
        
    @api.onchange('quantity', 'price','product_id','order_quantity')
    def _compute_total(self):
    # this function calculate the price according to amount of product the user use not all quantity
        for record in self:
            record.total = record.order_quantity * record.price
            
    
    # @api.onchange('quantity')
    # def _compute_total(self):
    #     for record in self:
    #         record.total = record.quantity * record.price        
    
    

    
            
            
            
            
