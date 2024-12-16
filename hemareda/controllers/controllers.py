# -*- coding: utf-8 -*-
# from odoo import http


# class Hemareda(http.Controller):
#     @http.route('/hemareda/hemareda', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hemareda/hemareda/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hemareda.listing', {
#             'root': '/hemareda/hemareda',
#             'objects': http.request.env['hemareda.hemareda'].search([]),
#         })

#     @http.route('/hemareda/hemareda/objects/<model("hemareda.hemareda"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hemareda.object', {
#             'object': obj
#         })
