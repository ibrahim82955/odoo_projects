from odoo import fields, api, _, models
from datetime import date


class wizard_data(models.TransientModel):
    _name = 'wizard.cancel'

    
    name = fields.Char(readonly=True)
    reason = fields.Text()
    pateint_idd = fields.Many2one('om_hospital.patient')

    # @api.onchange("name")
    # def hema(self):
    #     active_id = self.env.context.get('active_id')

    #     technical_order = self.env['om_hospital.patient'].browse(active_id)
    #     self.name = technical_order.name
        
        
        
    def cancel_reason(self):
        active_id = self.env.context.get('active_id')

        if active_id:
            technical_order = self.env['om_hospital.patient'].browse(active_id)
            self.name = technical_order.name
            technical_order.write({
                'reason': self.reason,
                'state': 'cancel'

            })
