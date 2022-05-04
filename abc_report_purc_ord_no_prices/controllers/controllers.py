# -*- coding: utf-8 -*-
# from odoo import http


# class AbcReportPurcOrdNoPrices(http.Controller):
#     @http.route('/abc_report_purc_ord_no_prices/abc_report_purc_ord_no_prices/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_report_purc_ord_no_prices/abc_report_purc_ord_no_prices/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_report_purc_ord_no_prices.listing', {
#             'root': '/abc_report_purc_ord_no_prices/abc_report_purc_ord_no_prices',
#             'objects': http.request.env['abc_report_purc_ord_no_prices.abc_report_purc_ord_no_prices'].search([]),
#         })

#     @http.route('/abc_report_purc_ord_no_prices/abc_report_purc_ord_no_prices/objects/<model("abc_report_purc_ord_no_prices.abc_report_purc_ord_no_prices"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_report_purc_ord_no_prices.object', {
#             'object': obj
#         })
