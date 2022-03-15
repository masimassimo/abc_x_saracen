odoo.define('bi_pos_credit_payment_offline.pos', function (require) {
	"use strict";

	var models = require('point_of_sale.models');

	models.load_fields('res.partner', ['custom_credit']);
	models.load_fields('pos.payment.method', ['credit_jr','cash_journal_id']);

	let OrderSuper = models.Order.prototype;
	models.Order = models.Order.extend({
		initialize: function(attributes, options) {
			OrderSuper.initialize.apply(this, arguments);
			let self = this;
			setInterval(function(){ 
				self.pos.load_new_partners();
			}, 5000);
		},
	});

});
