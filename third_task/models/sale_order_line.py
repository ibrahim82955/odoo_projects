from odoo import models, fields, api


class sale_order_line(models.Model):
    _inherit='sale.order.line'
    
    
    product_account =fields.Many2one('account.account',string='account id')
    dicsount  = fields.Float()
    
    
    def _prepare_invoice_line(self,**optional_values):
        res = super()._prepare_invoice_line(**optional_values)
        print("sdsadsadsd",self.order_id.partner_id.allowed_discount)
        res['discountt_inherit']=self.order_id.partner_id.allowed_discount
        return res
    
    
    