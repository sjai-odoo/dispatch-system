# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tools.sql import column_exists, create_column
from odoo import _, api, Command, fields, models

class StockPickingBatch(models.Model):
    _inherit = "stock.picking"
    
    volume_per_transfer = fields.Float()