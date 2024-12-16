from odoo import models, fields,api,_
class rejection_reason(models.TransientModel):
    
    _name = "technical__order.rejection_reason"
    
    
    rejection_reason = fields.Text(string='Rejection Reason')




    # def create_hema_rejection(self):
        # vals = {
        #     'state': self.st,
        #     'rejection_reason':self.rejection_reason
        #     }
        # # self..message_post(body="Test string ", subject="Appointment Creation")
        # new_appointment = self.env['technical_order.orders'].create(vals)
            
        
    def create_hema_rejection(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            technical_order = self.env['technical_order.orders'].browse(active_id)
            technical_order.write({
                'rejection_reason': self.rejection_reason,
                'state': 'reject'
            })    
       
        