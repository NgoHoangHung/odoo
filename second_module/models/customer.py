from odoo import fields, models, api

class Customer(models.Model):
    _inherit = 'customer'

    description = fields.Text(string="Description")
    phone = fields.Char(string="Phone")
