from odoo import models, fields, api


class Customer(models.Model):
    _name = 'customer'
    
    name = fields.Char(string='Họ Tên')
    address = fields.Char('Địa chỉ')
    age = fields.Integer('Tuổi')
    order_ids = fields.One2many('order','customer_id',string = 'ListOrder') 
    
    # # product_id = fields.One2Many('product','category_id',string ='Category Nums')

    # @api.model
    # def create(self, vals):
    #     vals['name'] = vals['name'].title()
    #     record = super(Category, self).create(vals)
    #     return record

    # def write(self, vals):
    #     result = super(Category, self).write(vals)
    #     return result

    # def unlink(self):
    #     return super(Category, self).unlink()
