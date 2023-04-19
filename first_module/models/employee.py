from odoo import models, fields, api


class Employee(models.Model):
    _name = 'employee'

    name = fields.Char(string='Nhân viên')
    active = fields.Boolean(default=True, string="Active")
    state = fields.Selection(string='Trạng Thái',
        selection=[('0', 'Đang làm việc'), ('1', 'Nghỉ Thai Sản'),
                   ('2', 'Nghỉ Phép'), ('3', 'Nghỉ Việc')]
        )

    def active_deactive(self):
            self.active = not self.active
    def leave(self):
        self.state = '1'

    def work(self):
        self.state = '0'
      