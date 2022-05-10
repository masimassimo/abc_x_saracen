# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError

class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = "purchase.order"
    
#    rfq_trg_resent = fields.Boolean("RFQ Resent Trigger", default=False, copy=False)
#    oda_trg_sent = fields.Boolean("ODA Sent Trigger", default=False, copy=False)

#    def write(self, vals):
#        if 'state' in vals:
#            new_value = vals['state']
#            old_value = self.state
#            if new_value != old_value and new_value == 'sent':
#                self.send_email_copy()
#                
#        res = super(PurchaseOrder, self).write(vals)
#        return res
    
    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        if self.env.context.get('mark_rfq_as_sent'):
            self.send_email_copy()
        return super(PurchaseOrder, self).message_post(**kwargs)
    
    def send_email_copy(self):
        for record in self:
            ir_model_data = self.env['ir.model.data']
            template_id = ir_model_data.get_object_reference('abc_send_rfq_copy', 'email_template_edi_purchase_zappala')[1]
            template = self.env['mail.template'].browse(template_id)
            template.send_mail(record.id)
        
# class abc_send_rfq_copy(models.Model):
#     _name = 'abc_send_rfq_copy.abc_send_rfq_copy'
#     _description = 'abc_send_rfq_copy.abc_send_rfq_copy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class PurchaseOrderLine(models.Model):
    _name = 'purchase.order.line'
    _inherit = 'purchase.order.line'
    
    def _prepare_values_on_req_qty(self):
    # Hook method to returns the different argument values for the
    # compute_all method, due to the fact that discounts mechanism
    # is not implemented yet on the purchase orders.
    # This method should disappear as soon as this feature is
    # also introduced like in the sales module.
    
        self.ensure_one()
        return {
            'price_unit': self.price_unit,
            'currency_id': self.order_id.currency_id,
            'product_qty': self.product_qty,
            'product': self.product_id,
            'partner': self.order_id.partner_id,
        }

    def _compute_old_amount(self):
        for line in self:
            vals = line._prepare_values_on_req_qty()
            taxes = line.taxes_id.compute_all(
                vals['price_unit'],
                vals['currency_id'],
                vals['product_qty'],
                vals['product'],
                vals['partner'])
            return ({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })