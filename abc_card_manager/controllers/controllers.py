# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCardManager(http.Controller):
#     @http.route('/abc_card_manager/abc_card_manager/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_card_manager/abc_card_manager/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_card_manager.listing', {
#             'root': '/abc_card_manager/abc_card_manager',
#             'objects': http.request.env['abc_card_manager.abc_card_manager'].search([]),
#         })

#     @http.route('/abc_card_manager/abc_card_manager/objects/<model("abc_card_manager.abc_card_manager"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_card_manager.object', {
#             'object': obj
#         })
