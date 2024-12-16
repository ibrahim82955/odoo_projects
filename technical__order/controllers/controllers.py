# -*- coding: utf-8 -*-
# from odoo import http


# class TechnicalOrder(http.Controller):
#     @http.route('/technical__order/technical__order', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/technical__order/technical__order/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('technical__order.listing', {
#             'root': '/technical__order/technical__order',
#             'objects': http.request.env['technical__order.technical__order'].search([]),
#         })

#     @http.route('/technical__order/technical__order/objects/<model("technical__order.technical__order"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('technical__order.object', {
#             'object': obj
#         })
