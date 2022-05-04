odoo.define('bi_pos_credit_payment_offline.pos', function (require) {
	"use strict";

	var models = require('point_of_sale.models');

	models.load_fields('res.partner', ['custom_credit']);
	models.load_fields('pos.payment.method', ['credit_jr','cash_journal_id']);

});
