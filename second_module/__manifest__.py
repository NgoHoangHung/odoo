# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Second Module',
    'version': '15.1.0',
    'summary': 'Odoo Learn ',
    'author': 'Akio',
    'description': """
    learn odoo
    """,
    'category': 'Orther',
    'depends': [
    'first_module', 'sale'
    ],
    'data': [
      'views/customer_view.xml',
      'views/employee_view.xml',
      'views/res_partner_view.xml',
      'security/security.xml',
    ],
    'installable': True,
    'application': True,
}
 
