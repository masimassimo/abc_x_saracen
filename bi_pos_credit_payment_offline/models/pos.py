# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,tools, api, _
from datetime import date, time, datetime
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)
import psycopg2


class PosConfig(models.Model):
	_inherit = 'pos.config'
	
	invoice_credit_payment = fields.Selection([('full_amount', 'Full Amount(without credit)'), ('partial_amount', 'Partial Amount(with credit)')],string='',default='full_amount')


class account_journal(models.Model):
	_inherit = 'account.journal'

	credit_jr = fields.Boolean(string='POS Credit Journal')   


class account_journal(models.Model):
	_inherit = 'pos.payment.method'

	credit_jr = fields.Boolean(string='POS Credit Journal',related='cash_journal_id.credit_jr',readonly=False)  


class POSOrder(models.Model):
	_inherit = 'pos.order'
	
	credit_check = fields.Boolean('Credit')	

	@api.model
	def _process_order(self, order, draft, existing_order):
		res = super(POSOrder, self)._process_order(order, draft, existing_order)
		pos_order = self.browse(res)
		if pos_order :
			for pyl in pos_order.payment_ids:
				if pyl.payment_method_id.credit_jr == True:
					vals = {
						'pos_order_id': pos_order.id,
						'partner_id': pos_order.partner_id.id,
						'used_credit_amount' :pyl.amount,
						'date' : pos_order.date_order,
						'pos_order_amount' : pos_order.amount_total,
						'balance_credit_amount' : pos_order.partner_id.custom_credit,
					}
					self.env['credit.history'].sudo().create(vals)	
					pos_order.partner_id.write({
						'custom_credit': pos_order.partner_id.custom_credit - pyl.amount,
					})
		return res

	def action_pos_order_invoice(self):
		moves = self.env['account.move']
		for order in self:
			invoice_credit_payment = order.config_id.invoice_credit_payment
			if invoice_credit_payment != 'partial_amount':
				return super(POSOrder, self).action_pos_order_invoice()
			else:
				if order.account_move:
					moves += order.account_move
					continue

				if not order.partner_id:
					raise UserError(_('Please provide a partner for the sale.'))

				move_vals = order._prepare_invoice_vals()
				new_move = order._create_invoice(move_vals)

				crd_amt = 0
				for pymt in order.payment_ids : 
					if pymt.payment_method_id.credit_jr:
						crd_amt += pymt.amount

				if crd_amt != 0 :
					new_move.update({'invoice_line_ids': [(0, 0, {
							'move_id': new_move.id,
							'quantity': 1,
							'name': 'Credit',
							'price_unit': - float(crd_amt),
							'account_id': self.env['account.account'].search([('internal_type','=', 'other')], limit=1).id, 				
						})]
					})

				order.write({'account_move': new_move.id, 'state': 'invoiced'})
				new_move.sudo().with_company(order.company_id)._post()
				moves += new_move

		if not moves:
			return {}

		return {
			'name': _('Customer Invoice'),
			'view_mode': 'form',
			'view_id': self.env.ref('account.view_move_form').id,
			'res_model': 'account.move',
			'context': "{'move_type':'out_invoice'}",
			'type': 'ir.actions.act_window',
			'nodestroy': True,
			'target': 'current',
			'res_id': moves and moves.ids[0] or False,
		}