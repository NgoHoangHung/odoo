from odoo import fields, models, api


class EmployeeLeaveReason(models.TransientModel):
    _name = 'employee.leave.reason'

    reason = fields.Selection(string='Trạng Thái',
                             selection=[('1', 'Nghỉ Thai Sản'),
                                        ('2', 'Nghỉ Phép'), ('3', 'Nghỉ Việc')]
                            )

    def update_leave_reason(self):
        return True
