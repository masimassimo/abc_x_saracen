# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from itertools import groupby
from pytz import timezone, UTC
from werkzeug.urls import url_encode

from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_is_zero
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang, format_amount

class PurchaseCalculateOnReceivedResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    calculate_on_received = fields.Boolean("Calculate amount on received quantity")
    
    def get_values(self):
        res = super(PurchaseCalculateOnReceivedResConfigSettings, self).get_values()
        res.update(
            calculate_on_received=self.env['ir.config_parameter'].sudo().get_param('abc_purchase_total_received.calculate_on_received'),
        )
        return res

    def set_values(self):
        super(PurchaseCalculateOnReceivedResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('abc_purchase_total_received.calculate_on_received', self.calculate_on_received)

class PurchaseOrderLine(models.Model):
    _name = 'purchase.order.line'
    _inherit = 'purchase.order.line'

    #NON SO SE SERVE
    @api.depends('product_qty', 'price_unit', 'taxes_id','qty_received')
    def _compute_amount(self):
        for line in self:
            vals = line._prepare_compute_all_values()
            taxes = line.taxes_id.compute_all(
                vals['price_unit'],
                vals['currency_id'],
                vals['product_qty'],
                vals['product'],
                vals['partner'])
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })
        
    def _prepare_compute_all_values(self):
        # Hook method to returns the different argument values for the
        # compute_all method, due to the fact that discounts mechanism
        # is not implemented yet on the purchase orders.
        # This method should disappear as soon as this feature is
        # also introduced like in the sales module.
        calculate_on_received = self.env['res.config.settings'].get_values()['calculate_on_received']
        if calculate_on_received:
            self.ensure_one()
            return {
                'price_unit': self.price_unit,
                'currency_id': self.order_id.currency_id,
                'product_qty': self.qty_received,
                'product': self.product_id,
                'partner': self.order_id.partner_id,
            }
        else:
            self.ensure_one()
            return {
                'price_unit': self.price_unit,
                'currency_id': self.order_id.currency_id,
                'product_qty': self.product_qty,
                'product': self.product_id,
                'partner': self.order_id.partner_id,
            }

