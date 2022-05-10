# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,tools, api, _
from datetime import date, time, datetime
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)
import psycopg2


class res_partner(models.Model):
	_inherit = 'res.partner'

	custom_credit = fields.Float('Credit')

	def action_view_credit_detail(self):
		self.ensure_one()

		partner_credit_ids = self.env['partner.credit'].search([('partner_id','=',self.id)])
		for payment_id in partner_credit_ids:
			self.env['partner.credit'].browse(payment_id)
			payment_id.do_update() 
		
		return {
			'name': 'Credit Details',
			'type': 'ir.actions.act_window',
			'view_mode': 'tree',
			'res_model': 'partner.credit',
			'domain': [('partner_id', '=', self.id)],
		}


class partner_credit(models.Model):
	_name = 'partner.credit'
	_description ="partner Credit"

	partner_id = fields.Many2one('res.partner',"Customer")
	credit_jr = fields.Float('Credit', readonly=True)
	update = fields.Float('Update')

	def do_update(self):
		
		update_credit_history_obj = self.env['update.credit.history']
		
		if self.update != 0:
			self.credit_jr = self.update
			val = {
				'date_update': datetime.now(),
				'update_credit_amount' : self.update,
				'old_credit_bal': self.partner_id.custom_credit,
				'balance': self.partner_id.custom_credit + self.update,
				'partner_id': self.partner_id.id,
			}
			update_credit_history_obj.create(val)
			self.partner_id.custom_credit = self.partner_id.custom_credit + self.credit_jr
			
		if self.partner_id.custom_credit != 0.00:
			
			self.credit_jr = self.partner_id.custom_credit
		self.update = 0.00                
	
	@api.onchange('partner_id')
	def onchange_partner_id(self):
		if self.partner_id:
			update = self.partner_id.update 
			return {'credit_jr':update}


class UpdateCreditHistory(models.Model):
	_name = 'update.credit.history'
	_description ="Update Credit History"
	
	date_update = fields.Date('Date')
	update_credit_amount = fields.Float('Update Credit amount')
	old_credit_bal = fields.Float('Old Credit Balance')
	balance = fields.Float('Balance')
	partner_id = fields.Many2one('res.partner', 'Customer')


class UpdateCreditHistoryPayment(models.Model):
	_name = 'update.credit.history.payment'
	_description ="Update Credit History Payment"
	
	date_update = fields.Date('Date')
	update_credit_amount = fields.Float('Update Credit amount')
	old_credit_bal = fields.Float('Old Credit Balance')
	payment_refer = fields.Many2one('account.payment', 'Payment Ref.')
	balance = fields.Float('Balance')
	partner_id = fields.Many2one('res.partner', 'Customer')


class UpdateCreditAccount(models.TransientModel):
	_name = 'credit.account'
	_description = "Credit Account"
	
	credit_amount = fields.Float('Credit Amount',required="True")
	journal_id = fields.Many2one('account.journal', 'Payment Journal',required=True,
		domain=[('type','in',['bank','cash']),('credit_jr','=',False)])
	credit_id = fields.Many2one('partner.credit', 'Customer')
	
	def post(self):
		context = self._context
		active_ids = context.get('active_ids')
		account_payment_obj = self.env['account.payment']
		partner_credit_id = self.env['partner.credit'].browse(active_ids[0])
		update_credit_payment_history_obj = self.env['update.credit.history.payment']
		
		date_now = datetime.strftime(datetime.now(), '%Y-%m-%d')
		
		vals = {}
		if self.credit_amount < 0:

			vals = {
				'name' : self.env['ir.sequence'].with_context(ir_sequence_date=date_now).next_by_code('account.payment.customer.invoice'),
				'payment_type' : "outbound",
				'amount' : -(self.credit_amount),
				'date' : datetime.now().date(),
				'journal_id' : self.journal_id.id,
				'payment_method_id': 1,
				'partner_type': 'supplier',
				'partner_id': partner_credit_id.partner_id.id,
			}

		if self.credit_amount >= 0.00:
			vals = {
				'name' : self.env['ir.sequence'].with_context(ir_sequence_date=date_now).next_by_code('account.payment.customer.invoice'),
				'payment_type' : "inbound",
				'amount' : self.credit_amount,
				'date' : datetime.now().date(),
				'journal_id' : self.journal_id.id,
				'payment_method_id': 1,
				'partner_type': 'customer',
				'partner_id': partner_credit_id.partner_id.id,
			}
		
		payment_create = account_payment_obj.create(vals)
		payment_create.action_post()
		if partner_credit_id.credit_jr >= 0.00:
			if payment_create.partner_type == 'customer':
				partner_credit_id.credit_jr = payment_create.amount
			
			if payment_create.payment_type == 'supplier':
				partner_credit_id.credit_jr = -(payment_create.amount)
			
			value = {
				'date_update': datetime.now(),
				'update_credit_amount' : partner_credit_id.credit_jr,
				'old_credit_bal': partner_credit_id.partner_id.custom_credit,
				'balance': partner_credit_id.partner_id.custom_credit + partner_credit_id.credit_jr,
				'partner_id': partner_credit_id.partner_id.id,
				'payment_refer' : payment_create.id,
			}
			update_credit_payment_history_obj.create(value)
			partner_credit_id.partner_id.custom_credit = partner_credit_id.partner_id.custom_credit + partner_credit_id.credit_jr
		
		if partner_credit_id.partner_id.custom_credit != 0.00:
			partner_credit_id.credit_jr = partner_credit_id.partner_id.custom_credit
		
		partner_credit_id.update = 0
		
		return



	