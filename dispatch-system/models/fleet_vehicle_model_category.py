from odoo import api, fields, models

class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string='Max Weight (kg)')
    max_volume = fields.Float(string='Max Volume (m3)')
