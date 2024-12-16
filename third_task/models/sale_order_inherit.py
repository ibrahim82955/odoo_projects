from odoo import models, fields, api
from odoo.exceptions import RedirectWarning, UserError, ValidationError



class sale_Order(models.Model):
    _inherit = 'sale.order'
   
    

    



    # @api.model
    # def create(self, vals_list):
    #     if self.partner_id.allowed_discount > 0:
    #         allowed_discount_product_id = int(self.env['ir.config_parameter'].sudo(
    #         ).get_param('third_task.allowed_discount_productt_id'))
    #         allowed_discount_account_idd = int(self.env['ir.config_parameter'].sudo(
    #         ).get_param('third_task.Allowed_discount_accountt_id'))
    #         print('32123132222', vals_list)
    #         product = self.env['product.product'].sudo().browse(
    #             allowed_discount_product_id)
    #         vals_list({
    #             'order_line':[{
    #                 'order_id': self.id,
    #                 'product_id': allowed_discount_product_id,
    #                 'product_template_id': allowed_discount_product_id,
    #                 'price_unit': -1 * self.partner_id.allowed_discount,
    #                 'name': 'allow',
    #                 'product_uom_qty': 1,
    #                 'product_uom': product.uom_id.id,
    #                 'product_account': allowed_discount_account_idd,
    #         }]
    #             })
    #     print('123323111',vals_list)
    #     return super( ).create(vals_list)

    # def action_confirm(self):
    #     # Call super to confirm the sale order
    #     res = super(sale_Order, self).action_confirm()

    #     for order in self:
    #         # Check if the customer has allowed discount
    #         partner = order.partner_id
    #         if partner and partner.allowed_discount > 0:
    #             allowed_discount_product_id = int(self.env['ir.config_parameter'].sudo(
    #             ).get_param('third_task.allowed_discount_productt_id'))
    #             allowed_discount_account_idd = int(self.env['ir.config_parameter'].sudo(
    #             ).get_param('third_task.Allowed_discount_accountt_id'))
    #             product = self.env['product.product'].sudo().browse(
    #                 allowed_discount_product_id)
    #             order_line = self.env['sale.order.line'].create({
    #                 'order_id': self.id,
    #                 'product_id': allowed_discount_product_id,
    #                 'product_template_id': allowed_discount_product_id,
    #                 'price_unit': -1 * order.partner_id.allowed_discount,
    #                 'name': 'allow',
    #                 'product_uom_qty': 1,
    #                 'product_uom': product.uom_id.id,
    #                 'product_account': allowed_discount_account_idd,
    #             })

    #     return res

    @api.onchange('partner_id')
    def onchange_prtner_id(self):
            allowed_discount_product_id = int(self.env['ir.config_parameter'].sudo().get_param('third_task.allowed_discount_productt_id'))
            allowed_discount_account_id = int(self.env['ir.config_parameter'].sudo().get_param('third_task.Allowed_discount_accountt_id'))
            
            product = self.env['product.product'].sudo().browse(allowed_discount_product_id)
            # delete old discount
            for line in self.order_line:
                if line.name == "allow":
                    line.unlink()
            
            if self.partner_id.allowed_discount > 0 :
                self.order_line =self.order_line+self.env['sale.order.line'].new({
                    'order_id': self.id,
                    'product_id':allowed_discount_product_id,
                    'product_template_id':allowed_discount_product_id,
                    'price_unit': -1 * self.partner_id.allowed_discount,
                    'name':'allow',
                    'dicsount':self.partner_id.allowed_discount,
                    'product_uom_qty': 1,
                    'product_uom': product.uom_id.id,
                    'product_account': allowed_discount_account_id,
                })                   
               

            

            
