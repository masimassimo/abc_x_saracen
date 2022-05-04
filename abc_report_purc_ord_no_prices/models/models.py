# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class abc_report_purc_ord_no_prices(models.Model):
#     _name = 'abc_report_purc_ord_no_prices.abc_report_purc_ord_no_prices'
#     _description = 'abc_report_purc_ord_no_prices.abc_report_purc_ord_no_prices'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
