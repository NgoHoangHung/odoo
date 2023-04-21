from odoo import fields, models, api


class EmployeeLeaveReason(models.TransientModel):
    _inherit = 'employee.leave.reason'

    def update_leave_reason(self):
        super(EmployeeLeaveReason, self).update_leave_reason()
        if self.reason == '3':
            employee_id = self.env.context.get('active_id', False)
            employee_record = self.env['employee'].browse(employee_id)
            employee_record.write({'active': False})
