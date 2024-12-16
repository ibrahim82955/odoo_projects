from odoo import fields,api,_,models
from datetime import date



class appointment(models.Model):
    _name='om_hospital.appointment'
    _inherit=['mail.activity.mixin','mail.thread']
    _rec_name='pateint_id'

    
    pateint_id=fields.Many2one(comodel_name="om_hospital.patient",string='pateint_id',tracking=True)
    gender =fields.Selection(related='pateint_id.gender',tracking=True)
    appointment_data=fields.Datetime(default=fields.Datetime.now,tracking=True)
    date_of_birth=fields.Date(string='birth day',tracking=True)
    age =fields.Float(string='age',compute='_compute_age',tracking=True)
    ref  = fields.Integer(compute='_compute_ref',tracking=True)
    
    @api.onchange('pateint_id')
    def _compute_ref(self):
        for rec in self:
            rec.ref =rec.pateint_id.refrence 
        
    def _compute_age(self):

        today=date.today()        
        if self.date_of_birth:
            self.age=today.year - self.date_of_birth.year
            
        else:
            self.age=0
            

            
        
    