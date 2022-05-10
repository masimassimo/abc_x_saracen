# -*- coding: utf-8 -*-
# from odoo import http


# class AbcSendRfqCopy(http.Controller):
#     @http.route('/abc_send_rfq_copy/abc_send_rfq_copy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_send_rfq_copy/abc_send_rfq_copy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_send_rfq_copy.listing', {
#             'root': '/abc_send_rfq_copy/abc_send_rfq_copy',
#             'objects': http.request.env['abc_send_rfq_copy.abc_send_rfq_copy'].search([]),
#         })

#     @http.route('/abc_send_rfq_copy/abc_send_rfq_copy/objects/<model("abc_send_rfq_copy.abc_send_rfq_copy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_send_rfq_copy.object', {
#             'object': obj
#         })
