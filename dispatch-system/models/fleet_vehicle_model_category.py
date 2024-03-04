from odoo import api, fields, models

class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string='Max Weight (kg)')
    max_volume = fields.Float(string='Max Volume (m3)')

    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
        self.display_name = self.name + " ( " + str(self.max_weight) + "kg, " + str(self.max_volume) + " m3 )"