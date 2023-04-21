from odoo import fields, models, api


class Employee(models.Model):
    _inherit = 'employee'

    experience = fields.Integer(string="Experience")

