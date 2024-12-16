# -*- coding: utf-8 -*-

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError, UserError


class orders(models.Model):
    _name = "technical_order.orders"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    
    Sequences = fields.Char(string='Sequence' ,readonly=True)
    Request_name = fields.Char(string='Request name',required=True,tracking=True)
    Requested_by = fields.Many2one('res.users',string='Requested by',default=lambda self: self.env.user,tracking=True)
    customer= fields.Many2one('res.partner',string='Customer',required=True,domain=[ ('set_the_value', '=', True)])
    start_date = fields.Date(string='Start Date',default=lambda self: fields.Date.today(),tracking=True)
    End_Date  = fields.Date(string='End_Date' ,tracking=True)
    state = fields.Selection([ ('draft','draft'),('to_be_approved', 'to_be_approved'), ('approved', 'approved'),('reject','reject'),('cancel','cancel')], default='draft')
    rejection_reason = fields.Text(string='Rejection Reason',readonly=True )
    OrderLine_ids  = fields.One2many(comodel_name='technical_order.line',inverse_name='order_id', string='Order Lines')
    total_price = fields.Float(string='Total', compute='_compute_total_price', store=True, readonly=True)
    order_count = fields.Integer(compute="compute_order_count")
    check  =   fields.Boolean(defaul=True  , readonly=True )

    # orders_id = fields.Many2one(
    #     'sale.order',
    #     string='orders_id' )
    # OrderLine_ids_change  = fields.Integer(compute='compute_remining_quantity')


    # group_sales =fields.Many2one(comodel_name='data.module_category_orders.group_sales_manager')
    
    
    @api.onchange('OrderLine_ids')
    def _compute_total_price(self):
        for order in self:
            hema = sum(order_line.total for order_line in order.OrderLine_ids)
            order.total_price = hema
            
    
    @api.model
    def create(self, vals):
        for rec in self:
            vals['Sequences'] = rec.env['ir.sequence'].next_by_code('meter.conf.seq')
            active_id = rec.env.context.get('active_id')
        return super(orders, self).create(vals)

        for s in self.OrderLine_ids:
            vals[s.order_id]=self.env['technical_order.orders'].browse(active_id).id
            
            
            
            
        
            
    
    
    
    def action_to_be_approved(self):
        for rec in self:
            rec.state = 'to_be_approved'
        # rainbow massage
        
        for xx in self.OrderLine_ids:
            xx.remining_order=xx.quantity
            if xx.quantity<0 or xx.order_quantity>xx.remining_order or xx.remining_order <0:
                raise ValidationError("you make mistake")
        return{
	        'effect': {
	        'fadeout': 'fast',
            'message': 'to_be_approved',
            'type': 'rainbow_man',
            } 
        }


            
           

        
        
        
        
        
    # def action_approved(self):
        
    #     sales_manager_group = self.env.ref('technical__order.group_sales_manager')  # Replace with the actual group ID

    #     if sales_manager_group:
    #         sales_manager_users = sales_manager_group.users

    #         # Extract email addresses from the users
    #         email_addresses = [user.email for user in sales_manager_users ]

    #         # Send the email to the list of email addresses
    #         email_template = self.env.ref('technical__order.approved_email_template')  # Replace with the actual template name
    #         email_template.email_to = ','.join(email_addresses)  # Set the 'email_to' field to a comma-separated list of email addresses
    #         email_template.send_mail(0)  # Send the email
        
            
    def action_approved(self):
        template_id=self.env.ref("technical__order.approved_email_template").id
        template=self.env['mail.template'].browse(template_id)
        template.send_mail(self.id,force_send=True)
        for rec in self:
            rec.state = 'approved'
        
       
        
        
        
        return{
	        'effect': {
	        'fadeout': 'fast',
            'message': 'approved',
            'type': 'rainbow_man',
            } 
        }    
        
        
        
        
            
            
    # def action_reject(self):
    #     for rec in self:
    #         rec.state = 'reject'
            
            
            
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
            
        return{
	        'effect': {
	        'fadeout': 'fast',
            'message': 'cancel',
            'type': 'rainbow_man',
            } 
        }
    
    
    
    
    def action_reset(self):
        for rec in self:
            rec.state = 'draft'    
        return{
	        'effect': {
	        'fadeout': 'fast',
            'message': 'reset to draft is confirmed',
            'type': 'rainbow_man',
            } 
        }    
            
    
    
    
    
    
    def create_sale_order(self):  
        # to_data used in so
         
        if  self.OrderLine_ids.order_quantity<self.OrderLine_ids.remining_order and self.OrderLine_ids.remining_order >0 :
            for rec in self:    
                sale_order = rec.env['sale.order'].create({
            'technicalorde_id': rec.id,
            'partner_id': rec.customer.id,
            'validity_date':rec.End_Date,
            'date_order':rec.start_date,
            'total_price':rec.total_price
        })
        else :
            raise ValidationError("cant't continue")    
                
    # one2many fields
        for x in self.OrderLine_ids:
            if x.quantity>0 and x.order_quantity<x.remining_order and x.remining_order >0:
                sale_order.order_line.create({
                    'order_id': sale_order.id,
                    'product_template_id':x.product_id.name,
                    'product_id':x.product_id.id,
                    'name':x.description,
                    'product_uom_qty':x.order_quantity
                    })
                x.remining_order -=x.order_quantity
                
                if x.remining_order==0:
                    self.check=False
                    raise ValidationError ("this product is finished")
                    
                
                    
                
                
                
                
    # @api.onchange(self.env['sale.order'].order_line.product_uom_qty)
    # def quantitttty(self)
                
    #             if sale_order.order_line.product_uom_qty > x.quantity :
    #                 raise ValidationError("quantity is incorrect")

            
                

    
    # @api.onchange(self.env['sale.order'].order_line)
    # def compute_remining_quantity(self):
    #     for record in sale_order.order_line:
    #         print('adsdsddsddddddddddddddddddd',record.product_uom_qty)
    
        
        
    def compute_order_count(self):
        for rec in self:
            rec.order_count = self.env['sale.order'].search_count([('technicalorde_id', '=', rec.id)])

    def action_open_units(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'orders',
            'res_model': 'sale.order',
            'domain': [('technicalorde_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
        



