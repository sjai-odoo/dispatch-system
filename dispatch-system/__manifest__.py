#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'stock-transport',
    # 'category': 'industry/real estate',
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
    ]
}