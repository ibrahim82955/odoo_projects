# # -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class hemareda(models.Model):
#     _name = 'hemareda.hemareda'
#     _description = 'hemareda.hemareda'

#     name = fields.Char(string ="coursename",required=True,
#     index=True
#     )
#     description = fields.Text()
#     number = fields.Integer(string='your number',required=True)    
#     city=fields.Selection(
#         string='choose',
#         selection=[('one', 'cairo'), ('two', 'giza')]
#     )
    
    
    
# #     value = fields.Integer()
# #     value2 = fields.Float(compute="_value_pc", store=True)
# #     description = fields.Text()
# #
# #     @api.depends('value')
# #     def _value_pc(self):
# #         for record in self:
# #             record.value2 = float(record.value) / 100
