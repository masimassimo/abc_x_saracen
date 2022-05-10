# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import UserError


class ResPartnerCardManager(models.Model):
    _name = 'res.partner.card_manager'
    _description = 'res.partner.card_manager'

    
    @api.depends("client_id")
    def _compute_price_list(self):
        for record in self:
            if(record.client_id):
                #raise UserError(self.env['res.partner'].search([['id','=', record.client_id.id]]))
                record.price_list = self.env['res.partner'].search([['id','=', record.client_id.id]]).property_product_pricelist
            else:
                record.price_list = None
                
    
    @api.depends("client_id")
    def _compute_date_activation(self):
        for record in self:
            if(record.client_id):
                record.date_activation = datetime.today()
            else:
                record.date_activation = None
                record.date_expiration = None
    
    @api.depends("client_id")
    def _compute_state(self):
        for record in self:
            if(record.client_id):
                record.state = True
            else:
                record.state = False
                
    @api.onchange("client_id")
    def _compute_barcode(self):
        
        for record in self:
            if(record.client_id):
                
                self.env['res.partner'].search([['id','=', record.client_id.id]]).barcode = record.name                
            else:
                
                self.env['res.partner'].search([['barcode','=', record.name]]).barcode = None
                
    name = fields.Char(string="ID Carta", help = "Il nome dato alla carta.", store=True, required=True, tracking=True, index = True, copy = False, default=lambda self: _('New'))
    state = fields.Boolean(string="Stato", help = "Lo stato della carta.", store=True, tracking=True, index = True, copy = False, compute=_compute_state)
    date_activation = fields.Date(string="Data attivazione", help = "La data di attivazione della carta.", store=True, tracking=True, index = True, copy = False, compute=_compute_date_activation)
    date_expiration = fields.Date(string="Data scadenza", help = "La data di scadenza della carta.", store=True, tracking=True, index = True, copy = False)
    client_id = fields.Many2one(comodel_name="res.partner", inverse_name="name", string="Cliente", help = "Il cliente della carta.", store=True, tracking=True, index = True, copy = False)
    saldo = fields.Float(string="Saldo", help = "Il saldo della carta.", store=True, tracking=True, index = True, copy = False)
    price_list = fields.Many2one(comodel_name="product.pricelist", inverse_name="name", string="Listino Prezzi", help = "Il listino del cliente della carta.", store=True, tracking=True, index = True, copy = False, compute=_compute_price_list)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.user.company_id.currency_id)
    

