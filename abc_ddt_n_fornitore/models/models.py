# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockDeliveryNote(models.Model):
    _name = "stock.delivery.note"
    _inherit = "stock.delivery.note"
    
    n_ddt_fornitore = fields.Char(string="N° DDT Fornitore")

class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = "stock.picking"
    
    n_ddt_fornitore = fields.Char(string="N° DDT Fornitore", related='delivery_note_id.n_ddt_fornitore', readonly=False)
    
            
#class StockDeliveryNoteCreateWizard(models.TransientModel):
#    _name = "stock.delivery.note.create.wizard"
#   _inherit = "stock.delivery.note.create.wizard"
    
    
# class abc_ddt_expiration(models.Model):
#     _name = 'abc_ddt_expiration.abc_ddt_expiration'
#     _description = 'abc_ddt_expiration.abc_ddt_expiration'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
