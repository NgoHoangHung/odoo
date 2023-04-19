from odoo import models, fields, api


class ProductCategories(models.Model):
    _name = 'product.categories'
    _rec_name = 'cate_name'

    cate_name = fields.Char(string='Name')
    description = fields.Char('Mô tả')
    product_ids = fields.One2many(
        'product', 'category_id', string="Product")
    product_count = fields.Integer(
        compute='get_product_count', string='Product Count', store=True)

    @api.depends('product_ids')
    def get_product_count(self):
        for category in self:
            category.product_count = len(category.product_ids)
