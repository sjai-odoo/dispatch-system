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
    start_date = fields.Date(string='Start Date', default=lambda self: datetime.today() - relativedelta(days=6))
    end_date = fields.Date(string='End Date', default=datetime.today())

    @api.depends('move_line_ids.product_id','vehicle_category_id')
    def _compute_weight(self):
        total=0
        for record in self:
            for subline in record.move_line_ids: #line
                total = total + (subline.product_id.weight * subline.quantity)

            if(record.vehicle_category_id and record.vehicle_category_id.max_weight != 0):
                record.weight = (total/record.vehicle_category_id.max_weight)*100
            else:
                record.weight=0
    
    @api.depends('move_line_ids.product_id','vehicle_category_id')
    def _compute_volume(self):
        total=0
        for record in self:
            for subline in record.move_line_ids: #line
                total = total + (subline.product_id.volume * subline.quantity)
        
            if(record.vehicle_category_id and record.vehicle_category_id.max_volume != 0):
                record.volume = (total/record.vehicle_category_id.max_volume)*100
            else:
                record.volume=0

    @api.depends('vehicle_category_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} (  {record.vehicle_category_id.max_weight} kg, {record.vehicle_category_id.max_volume}  m3 ) "