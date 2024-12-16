from odoo import models, api, _, fields


class patientt(models.Model):
    _name = 'om_hospital.patient'
    _inherit = ['mail.activity.mixin', 'mail.thread']
    _description = 'patient'
    Sequences = fields.Char()
    name = fields.Char(string='name', tracking=True)
    age = fields.Float(string='age', tracking=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], tracking=True)
    refrence = fields.Char(string='ref', tracking=True)
    prescription = fields.Html()
    priority = fields.Selection([
        ('clear', 'Clear'),
        ('urgent', 'Urgent'),
        ('normal', 'Normal'),
        ('lowand', 'Lowand'),
        ('high', 'High')], tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consaltant', 'In consaltant'),
        ('approve', 'Approve'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], tracking=True, default='draft')
    image = fields.Image(string='image')

    fine = fields.Boolean(string='are you fine')

    reason = fields.Text(string='reason')

    _sql_constraints = [
        ('age_check',
         'CHECK(age >=10.0)',
         'Notification time must be between 0 and 12'),
        ('name_unique', 'unique(name)', "Direct Debit Instruction identifier must be unique! Please choose another one.")
    ]
    def return_to_draft(self):
        for rec in self:
            rec.state = 'draft'

    def in_consaltant(self):
        for rec in self:
            rec.state = 'in_consaltant'

    def approve(self):
        for rec in self:
            rec.state = 'approve'

    def done(self):
        for rec in self:
            rec.state = 'done'

    # def cancel(self):
    #     for rec in self :
    #         rec.state='cancel'

    #  return{
    # 	        'effect': {
    # 	        'fadeout': 'fast',
    #             'message': 'to_be_approved',
    #             'type': 'rainbow_man',
    #             }
    #         }
    @api.model
    def create(self, vals):
        vals['Sequences'] = self.env['ir.sequence'].next_by_code('meter.conf.seq')
        print('asdasdasdd')
        return super(patientt, self).create(vals)

    def name_get(self):
        # name get function for the model executes automatically
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.name, rec.Sequences)))
        return res
