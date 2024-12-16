from odoo import fields, models, api, _
from datetime import date
from odoo.exceptions import RedirectWarning, UserError, ValidationError



class ResUsers(models.Model):
    _inherit = 'res.partner'
    national_id = fields.Char()
    age = fields.Integer(compute='_compute_age')

    @api.onchange('national_id')
    def _compute_age(self):
        for order in self:
            # day
            today = date.today().year
            today = today-2000
            a = int(self.national_id[1:3])
            # --------------------------------
            # month
            month = date.today().month
            b = int(self.national_id[3:5])
            print('aaaaaaaaa', b)

            if (self.national_id[0] == '2'):
                if(b>month):
                    print('enter')
                    self.age = ((99-a)+today)
                else:    
                    self.age = (100-a)+today


            elif (self.national_id[0] == '3'):
                if(b>month):
                    self.age = (today-a)-1
                else:
                    self.age = (today-a)



            else:
                raise ValidationError('you are died')
