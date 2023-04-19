# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'First Module',
    'version': '1.0',
    'summary': 'Odoo Learn ',
    'sequence': 1,
    'author': 'Akio',
    'description': """
    learn odoo
    """,
    'category': 'Orther',
    'website': '',
    'depends': ['purchase'],
    'data': [
        'wizard/employee_leave_reason_view.xml',
        'views/product_category_view.xml',
        'views/customer_view.xml',
        'views/product_view.xml',
        'views/supplier_view.xml',
        'views/employee_view.xml',
        'views/order_view.xml',
        'views/order_line_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'auto_upgrade': True,
}
