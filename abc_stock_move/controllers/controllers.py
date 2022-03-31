# -*- coding: utf-8 -*-
# from odoo import http


# class AbcStockMove(http.Controller):
#     @http.route('/abc_stock_move/abc_stock_move/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_stock_move/abc_stock_move/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_stock_move.listing', {
#             'root': '/abc_stock_move/abc_stock_move',
#             'objects': http.request.env['abc_stock_move.abc_stock_move'].search([]),
#         })

#     @http.route('/abc_stock_move/abc_stock_move/objects/<model("abc_stock_move.abc_stock_move"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_stock_move.object', {
#             'object': obj
#         })
