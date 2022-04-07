# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError
import datetime

class StockMoveLine(models.Model):
    _name = "stock.move.line"
    _inherit = "stock.move.line"

    expiration_date_upd = fields.Date(string="Data Scadenza")
    
    @api.depends('expiration_date_upd')
    def _manual_expiration_date(self):
        for record in self:
            if (record.expiration_date_upd != False):
                record.expiration_date = record.expiration_date_up
                
    #OVERRIDE DELLA FUNZIONE ORIGINALE
    @api.depends('product_id', 'picking_type_use_create_lots')
    def _compute_expiration_date(self):
        for move_line in self:
            if move_line.picking_type_use_create_lots:
                if move_line.product_id.use_expiration_date:
                    if not move_line.expiration_date:
                        if (move_line.expiration_date_upd != False):
                            move_line.expiration_date = move_line.expiration_date_upd
                        else:
                            move_line.expiration_date = fields.Datetime.today() + datetime.timedelta(days=move_line.product_id.expiration_time)
                else:
                    move_line.expiration_date = False
                    
    def _assign_production_lot(self, lot):
        super()._assign_production_lot(lot)
        if (self[0].expiration_date_upd != False):
            self[0].expiration_date = self[0].expiration_date_upd
        
        self.lot_id._update_date_values(self[0].expiration_date)
    
    #@api.onchange('lot_id')
    #def _onchange_lot_id(self):
    #    raise UserError('assign')
    #    if not self.picking_type_use_existing_lots or not self.product_id.use_expiration_date:
    #        return
    #    if self.lot_id:
    #        self.expiration_date = self.lot_id.expiration_date
    #    else:
    #        self.expiration_date = False