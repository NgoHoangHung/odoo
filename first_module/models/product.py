from odoo import models, fields, api, exceptions
from datetime import datetime


class Product(models.Model):
    _name = 'product'

    def get_default_purchase_date(self):
        return datetime.now()

    name = fields.Char(string='Tên Sản Phẩm')
    price = fields.Integer(string='Giá Bán')
    purchase_date = fields.Datetime(
        string='Ngày Nhập Hàng', default=get_default_purchase_date)
    warranty = fields.Selection(
        selection=[('warranty', 'Bảo Hành'), ('not', 'Không Bảo Hành')], string='Warranty')
    vat = fields.Float(default=0.1, string='VAT')
    price_wth_tax = fields.Float(
        string='Giá Sau Thuế ', compute='get_price_wth_tax')
    active = fields.Boolean(string='Active', default=True)
    category_id = fields.Many2one(
        comodel_name='product.categories', string='Category')
    supplier_ids = fields.Many2many(comodel_name='supplier', relation='supplier_product_rel', column2='supplier_id',
                                    column1='product_id', string='Supplier')

    @ api.depends('vat', 'price')
    def get_price_wth_tax(self):
        for product in self:
            if product.vat:
                product.price_wth_tax = product.price + product.price*product.vat
            else:
                product.price_wth_tax = product.price

    @ api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Product, self).create(vals)
        return record

    def write(self, vals):
        result = super(Product, self).write(vals)
        return result

    def unlink(self):
        return super(Product, self).unlink()

    # @api.constrains('price')
    # def validate_price(self):
    #     if not self.price or self.price <= 5:
    #         raise exceptions.ValidationError('Price need greater than 5')

    @ api.onchange('price')
    def onchange_price(self):
        if self.price and self.price > 10:
            self.warranty = 'warranty'
        else:
            self.warranty = 'not'

    def test(self):
        # trong python, việc khai báo các module khác ngoài module đang triển khai
        # là ta đang muốn sử dụng các class bên trong module ấy
        c = self.env['purchase.order']
        print(c)
