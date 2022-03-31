# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class abc_stock_move(models.Model):
#     _name = 'abc_stock_move.abc_stock_move'
#     _description = 'abc_stock_move.abc_stock_move'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
import json
from collections import defaultdict
from datetime import datetime
from itertools import groupby
from operator import itemgetter
from re import findall as regex_findall
from re import split as regex_split

from dateutil import relativedelta

from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools.float_utils import float_compare, float_is_zero, float_repr, float_round
from odoo.tools.misc import clean_context, format_date, OrderedSet

PROCUREMENT_PRIORITIES = [('0', 'Normal'), ('1', 'Urgent')]


class StockMove(models.Model):
    _name = "stock.move"
    _inherit = "stock.move"
    
    qty_origin = fields.Float('Q.tà Movimento origine', compute='_quantity_origin_compute')
    
    
    #REALIZZATO A PARTIRE DA stock_move.PY _quantity_done_compute
    @api.depends('move_orig_ids')
    def _quantity_origin_compute(self):
        output = ''
        for record in self:
            #VERIFICHIAMO SE NON E UN INSIEME
            record.qty_origin=0
            if not any(record._ids):
                for move in record.move_orig_ids:
                    quantity_done = 0
                    for move_line in move._get_move_lines():
                        quantity_done += move_line.product_uom_id._compute_quantity(
                            move_line.qty_done, move.product_uom, round=False)
                    record.qty_origin += quantity_done
            else:
                #CI SONO PIU ID
                # compute
                move_lines_ids = set()
                for move in record.move_orig_ids:
                    move_lines_ids |= set(move._get_move_lines().ids)      
                #LEGGIAMO I DATI DELLE LINEE DEI MOVIMENTI DI MAGAZZINO RAGGRUPPATI PER MOVE_ID E PRODUCT_UOM_ID   
                data = self.env['stock.move.line'].read_group(
                    [('id', 'in', list(move_lines_ids))],
                    ['move_id', 'product_uom_id', 'qty_done'], ['move_id', 'product_uom_id'],
                    lazy=False
                )
                
                #SI UTILIZZA DEFAULTDICT PER NON GENERARE UN KEY ERROR
                rec = defaultdict(list)
                
                for d in data:
                    rec[d['move_id'][0]] += [(d['product_uom_id'][0], d['qty_done'])]

                for move in record.move_orig_ids:
                    #SCORRE I MOVIMENTI DI ORIGINE E PER OGNUNO DI ESSI SOMMA LE QUANTITA DELLE LINEE
                    uom = move.product_uom
                                           
                    result = sum(
                        self.env['uom.uom'].browse(line_uom_id)._compute_quantity(qty, uom, round=False)
                         for line_uom_id, qty in rec.get(move.ids[0] if move.ids else move.id, [])
                    )
                    
                    #NON POSSIAMO FARE UN ASSEGNAZIONE DIRETTA DATO CHE ABBIAMO UTILIZZATO DEFAULT DICT
                    #INVECE CONTROLLIAMO IL RISULTATO E LO ASSEGNAMO SOLAMENTE SE E DIVERSO DA 0
                    if result != 0:
                        record.qty_origin = result
                   