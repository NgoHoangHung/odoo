from odoo import models, fields, api


class Supplier(models.Model):
    _name = 'supplier'

    name = fields.Char(string='Nhà Cung Cấp')
    product_ids = fields.Many2many(comodel_name='product', relation='supplier_product_rel', column1='supplier_id',
                                   column2='product_id', string='Procduct')

    # cách2 :  product_ids  = fields.Many2many(comodel_name= 'product',string = 'Procduct')

    # found_date = fields.Datetime(string='Ngày Thành Lập')
    # quality_level = fields.Selection(
    #     selection=[('1', 'Rất Thấp'),('2', 'Thấp'),('3', 'Trung Bình'),('4', 'Tốt'),('5', 'Rất Tốt')], string='Độ Uy Tín')

    # product_id = fields.One2Many('product','category_id',string ='Category Nums')

    # @api.model
    # def create(self, vals):
    #     vals['name'] = vals['name'].title()
    #     record = super(Supplier, self).create(vals)
    #     return record

    # def write(self, vals):
    #     result = super(Supplier, self).write(vals)
    #     return result

    # def unlink(self):
    #     return super(Supplier, self).unlink()
