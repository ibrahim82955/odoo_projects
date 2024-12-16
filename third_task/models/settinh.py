from odoo import models, fields, api


class discount(models.TransientModel):
    _inherit = 'res.config.settings'

    Allowed_discount_accountt_id = fields.Many2one('account.account', string='Allowed discount account',
                                                   required=True,
                                                   config_parameter='third_task.Allowed_discount_accountt_id',

                                                   store=True

                                                   )
    allowed_discount_productt_id = fields.Many2one('product.product', string='Allowed Discount Product', domain=[(
        'type', '=', 'service')], config_parameter='third_task.allowed_discount_productt_id', required=True, store=True)
