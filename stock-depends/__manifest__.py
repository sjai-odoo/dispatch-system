#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'stock-depends',
    # 'category': 'industry/real estate',
    'description': 'Transport Management System',
    'summary': 'Realestate property sell/buy',
    'depends': ['base', 'stock'],
    'installable': True,
    'application': True,
    'sequence': 2,
    'license': 'OEEL-1',
    'version': '1.0',
    'auto_install': True,
    'data' :[
        'views/res_config_settings.xml'
    ]
}