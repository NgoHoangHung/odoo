from odoo import fields, models, api


class Order(models.Model):
    _name = 'order'

    customer_id = fields.Many2one('customer', string='Customer')
    total_amount = fields.Float(string='Total Amount',compute ='_get_total_amount')
    order_line_ids = fields.One2many('order.line', 'order_id', string='Lines')

    # @api.depends(order_line_ids) ,store = "True" đang lỗi nếu cấu hình lại
    def _get_total_amount(self):
        for order in self:
            result = 0.0
            for line in self.order_line_ids:
                result += line.sub_total
            order.total_amount = result

    # @api.onchange('order_line_ids.sub_total')
    # def total(self):
    #     result = 0.0
    #     for line in self.order_line_ids:
    #         result += line.sub_total
    #     self.total_amount = result