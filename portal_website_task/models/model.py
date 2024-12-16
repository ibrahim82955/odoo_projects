from odoo import models, fields, api
from odoo.exceptions import RedirectWarning, UserError, ValidationError
from datetime import date


class models(models.Model):
    _name = "employ_attentance"

    name = fields.Char()
    check_in = fields.Datetime(string=" check in", required=False, default=fields.Datetime.now, tracking=True)
    check_out = fields.Datetime(string="check out", required=False, default=fields.Datetime.now, tracking=True)
