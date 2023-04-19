from odoo import fields, models, api


class OrderLine(models.Model):
    _name = 'order.line'
    
    order_id = fields.Many2one('order', string='Order')
    product_id = fields.Many2one('product', string='Product')
    qty = fields.Integer(string='Qty')
    amount = fields.Integer(string='Amount') 
    sub_total = fields.Integer(string='') 

    @api.onchange('qty','amount')
    def onchange_sub_total(self):
        if self.amount*self.qty != 0:
            self.sub_total = self.amount*self.qty 
        else:
            self.sub_total = 0