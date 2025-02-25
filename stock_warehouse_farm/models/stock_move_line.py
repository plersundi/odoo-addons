# Copyright 2022 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    picking_type_id = fields.Many2one(
        string='Type',
        comodel_name='stock.picking.type',
        related='move_id.picking_type_id',
        store=True)
    category_type_id = fields.Many2one(
        string='Category Type',
        comodel_name='category.type',
        related='picking_type_id.category_type_id',
        store=True)
