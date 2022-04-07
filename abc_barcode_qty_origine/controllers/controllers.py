# -*- coding: utf-8 -*-
# from odoo import http


# class AbcBarcodeQtyOrigine(http.Controller):
#     @http.route('/abc_barcode_qty_origine/abc_barcode_qty_origine/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_barcode_qty_origine/abc_barcode_qty_origine/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_barcode_qty_origine.listing', {
#             'root': '/abc_barcode_qty_origine/abc_barcode_qty_origine',
#             'objects': http.request.env['abc_barcode_qty_origine.abc_barcode_qty_origine'].search([]),
#         })

#     @http.route('/abc_barcode_qty_origine/abc_barcode_qty_origine/objects/<model("abc_barcode_qty_origine.abc_barcode_qty_origine"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_barcode_qty_origine.object', {
#             'object': obj
#         })
