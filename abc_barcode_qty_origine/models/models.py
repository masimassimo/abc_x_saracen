# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMoveLine(models.Model):
    _name = "stock.move.line"
    _inherit = "stock.move.line"

    move_qty_origin =fields.Float('Q.tà Movimento origine', compute='_quantity_origin_compute')
    
    @api.depends('move_id')
    def _quantity_origin_compute(self):
        for record in self:
            record.move_qty_origin = 0
            if (record.move_id != False):
                record.move_qty_origin = record.move_id.qty_origin
                
                
class StockInventoryLine(models.Model):
    _name = "stock.inventory.line"    
    _inherit = "stock.inventory.line"    
    
    move_qty_origin =fields.Float('Q.tà Movimento origine')
    
class StockPicking(models.Model):
    _name = 'stock.picking'
    _inherit = 'stock.picking'
    
    @api.model
    def _get_move_line_ids_fields_to_read(self):
        """ read() on picking.move_line_ids only returns the id and the display
        name however a lot more data from stock.move.line are used by the client
        action.
        """
        return [
            'product_id',
            'location_id',
            'location_dest_id',
            'qty_done',
            'display_name',
            'product_uom_qty',
            'product_uom_id',
            'product_barcode',
            'owner_id',
            'lot_id',
            'lot_name',
            'package_id',
            'result_package_id',
            'dummy_id',
            'move_qty_origin'
        ]