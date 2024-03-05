#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'dispatch_system',
    'category': 'industry/dispatch',
    'description': 'Transport Management System',
    'summary': 'Realestate property sell/buy',
    'depends': ['fleet', 'stock_picking_batch'],
    'installable': True,
    'application': True,
    'sequence': 1,
    'license': 'OEEL-1',
    'version': '1.0',
    'data' : [
        'views/fleet_vehicle_model_category.xml',
        'views/stock_picking_batch.xml',
        'views/stock_picking.xml',
        'security/dispatch_system_groups.xml',
        'security/ir.model.access.csv',
    ]
}