from odoo import fields,api,_,models
from datetime import date

class saleOrder(models.Model):
    _inherit = 'sale.order'   
    
    
    
    
    
    
    def action_confirm(self):
        print("sfdfdshdfsdgff")

        super(saleOrder,self).action_confirm()
        
        
    @api.model
    def create(self,values):
        print(values)
        return super().create(values)
    
    
    
    