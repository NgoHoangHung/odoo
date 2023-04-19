from odoo import fields, models, api

class Order(models.Model):
    _name = 'order'

    customer_id = fields.Many2one('customer', string='Customer')
    total_amount = fields.Integer(string = 'Total Amount')
    order_line_ids = fields.One2many('order.line','order_id',string = 'Lines') 
    
