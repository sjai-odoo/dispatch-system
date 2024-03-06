from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('dispatch.dock')
    vehicle_id = fields.Many2one('fleet.vehicle',required=False)
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category',required=False)
    weight = fields.Float(compute="_compute_weight", store=True) # store = true wasn't there so can't convert to sql
    volume = fields.Float(compute="_compute_volume", store=True)
    end_date = fields.Datetime(string='End Date', compute="_compute_end_date", store=True)
    move_lines = fields.Integer(compute="_compute_move_lines", store=True) # can't run on duplication as scheduled date have copy false
    picking_lines = fields.Integer(compute="_compute_picking_lines", store=True)
    total_weight = fields.Float(compute="_compute_weight", store=True)
    total_volume = fields.Float(compute="_compute_volume", store=True)
    
    @api.depends('move_line_ids.product_id','vehicle_category_id')
    def _compute_weight(self):
        total=0
        for record in self:
            for subline in record.move_line_ids: #line
                total = total + (subline.product_id.weight * subline.quantity)
            record.total_weight = total
            record.weight = (total/record.vehicle_category_id.max_weight)*100 if(record.vehicle_category_id and record.vehicle_category_id.max_weight != 0) else 0
    
    @api.depends('move_line_ids.product_id','vehicle_category_id')
    def _compute_volume(self):
        total=0
        for record in self:
            for subline in record.move_line_ids: #line
                total = total + (subline.product_id.volume * subline.quantity)
            record.total_volume = total
            record.volume = (total/record.vehicle_category_id.max_volume)*100 if (record.vehicle_category_id and record.vehicle_category_id.max_volume != 0) else 0

    @api.depends('move_line_ids')
    def _compute_move_lines(self):
        for record in self:
            record.move_lines = len(record.move_line_ids) if self.picking_ids else 0
    
    @api.depends('picking_ids')
    def _compute_picking_lines(self):
        for record in self:
            record.picking_lines = len(record.picking_ids) if self.picking_ids else 0

    @api.depends('scheduled_date')
    def _compute_end_date(self):
        for record in self:
            if(not record.scheduled_date):
                record.end_date = datetime.today()
            else:
                record.end_date = record.scheduled_date + relativedelta(days=6)

    @api.depends('vehicle_category_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} (  {record.vehicle_category_id.max_weight} kg, {record.vehicle_category_id.max_volume}  m3 ) {record.vehicle_id.driver_id.name}"