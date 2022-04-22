# -*- coding: utf-8 -*-
# from odoo import http


# class AbcPurchaseTotalReceived(http.Controller):
#     @http.route('/abc_purchase_total_received/abc_purchase_total_received/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_purchase_total_received/abc_purchase_total_received/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_purchase_total_received.listing', {
#             'root': '/abc_purchase_total_received/abc_purchase_total_received',
#             'objects': http.request.env['abc_purchase_total_received.abc_purchase_total_received'].search([]),
#         })

#     @http.route('/abc_purchase_total_received/abc_purchase_total_received/objects/<model("abc_purchase_total_received.abc_purchase_total_received"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_purchase_total_received.object', {
#             'object': obj
#         })
