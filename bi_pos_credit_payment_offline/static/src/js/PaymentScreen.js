odoo.define('pos_credit_payment.PaymentScreenWidget', function(require){
	'use strict';

	const PaymentScreen = require('point_of_sale.PaymentScreen');
	const PosComponent = require('point_of_sale.PosComponent');
	const Registries = require('point_of_sale.Registries');
	const { Component } = owl;
	var rpc = require('web.rpc');

	const PaymentScreenWidget = (PaymentScreen) =>
		class extends PaymentScreen {
			constructor() {
				super(...arguments);
			}

			async validateOrder(isForceValidate) {
				
				var self = this;
				var currentOrder = this.env.pos.get_order();
				var plines = currentOrder.get_paymentlines();
				var dued = currentOrder.get_due();
				var changed = currentOrder.get_change();
				var clients = currentOrder.get_client();
				var a = [];
				var pos_cur =  this.env.pos.config.currency_id[0];
				var company_id = this.env.pos.config.company_id;

				var total_crdt = 0;
				for(var i = 0; i < plines.length; i++) {
					if(plines[i].payment_method.credit_jr === true){
						total_crdt += plines[i].amount;
						a.push(plines[i]);
					}
				}

				if(clients && total_crdt > clients.custom_credit){ 
					self.showPopup('ErrorPopup',{
						'title': self.env._t('Not Sufficient Credit'),
						'body': self.env._t('Customer has not Sufficient Credit To Pay'),
					});
					return;
				}

				if(currentOrder.get_orderlines().length === 0){
					self.showPopup('ErrorPopup',{
						'title': this.env._t('Empty Order'),
						'body': this.env._t('There must be at least one product in your order before it can be validated.'),
					});
					return;
				}
				 
				if (clients){ 
					if (a['length'] !== 0) { 
						for (var i = 0; i < plines.length; i++) {
							if(plines[i].payment_method.credit_jr === true){
								if (!currentOrder.get_client()){
									self.showPopup('ErrorPopup',{
										'title': this.env._t('Unknown customer'),
										'body': this.env._t('You cannot use Credit payment. Select customer first.'),
									});
									return;
								}

								if(currentOrder.get_change() > 0){
									   self.showPopup('ErrorPopup',{
										'title': this.env._t('Payment Amount Exceeded'),
										'body': this.env._t('You cannot Pay More than Total Amount'),
									});
									return;
								}
					
								var amount = plines[i].get_amount();
								if(amount > clients.custom_credit){ 
								   self.showPopup('ErrorPopup',{
										'title': self.env._t('Not Sufficient Credit'),
										'body': self.env._t('Customer has not Sufficient Credit To Pay'),
									});
									return;
								}
								else{
									clients.custom_credit -= amount;
									if (self._isOrderValid(isForceValidate)) {
										self._finalizeValidation();
									}
								}
							}
						}
					}else{
						if (await this._isOrderValid(isForceValidate)) {
							for (let line of this.paymentLines) {
								if (!line.is_done()) this.currentOrder.remove_paymentline(line);
							}
							await this._finalizeValidation();
						}
					}
					
				}else if(a['length'] == 0){
					if (await this._isOrderValid(isForceValidate)) {
						for (let line of this.paymentLines) {
							if (!line.is_done()) this.currentOrder.remove_paymentline(line);
						}
						await this._finalizeValidation();
					}
				}else{
					self.showPopup('ErrorPopup',{
						'title': this.env._t('Unknown customer/use credit payment'),
						'body': this.env._t('You cannot use Credit payment. Select customer first.'),
					});
					return;
				}       	                
			}
	};

	Registries.Component.extend(PaymentScreen, PaymentScreenWidget);
	return PaymentScreen;

});