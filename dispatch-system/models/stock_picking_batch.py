from odoo import api, fields, models

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    vehicle_id = fields.Many2one('fleet.vehicle',required=False)
    vehicle_category = fields.Many2one('fleet.vehicle.model.category',required=False)
    weight = fields.Float(compute="_compute_weight", default=0)
    volume = fields.Float(compute="_compute_volume")
    
    @api.depends('move_line_ids.product_id','vehicle_category')
    def _compute_weight(self):
        total=0
        for record in self:
            for subline in record.move_line_ids: #line
                total = total + (subline.product_id.weight * subline.quantity)
        if(self.vehicle_category and self.vehicle_category.max_weight != 0):
            self.weight = (total/self.vehicle_category.max_weight)*100
    
    @api.depends('move_line_ids.product_id','vehicle_category')
    def _compute_volume(self):
        total=0
        for record in self:
            for subline in record.move_line_ids: #line
                total = total + (subline.product_id.volume * subline.quantity)
        
        self.volume = (total/self.vehicle_category.max_weight)*100
