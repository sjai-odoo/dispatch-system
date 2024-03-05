from odoo import api, fields, models

class Docks(models.Model):
    _name = 'dispatch.dock'

    name = fields.Char()
    