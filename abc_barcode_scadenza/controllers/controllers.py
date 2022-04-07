# -*- coding: utf-8 -*-
# from odoo import http


# class AbcBarcodeScadenza(http.Controller):
#     @http.route('/abc_barcode_scadenza/abc_barcode_scadenza/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_barcode_scadenza/abc_barcode_scadenza/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_barcode_scadenza.listing', {
#             'root': '/abc_barcode_scadenza/abc_barcode_scadenza',
#             'objects': http.request.env['abc_barcode_scadenza.abc_barcode_scadenza'].search([]),
#         })

#     @http.route('/abc_barcode_scadenza/abc_barcode_scadenza/objects/<model("abc_barcode_scadenza.abc_barcode_scadenza"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_barcode_scadenza.object', {
#             'object': obj
#         })
