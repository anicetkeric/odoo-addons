# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, models
import logging
_logger = logging.getLogger(__name__)

class HrHolidays(models.Model):
    _inherit = 'hr.holidays'


    @api.model
    def create(self, vals):
        res = super(HrHolidays, self).create(vals)
        if res.employee_id.parent_id.user_id:
            template_id = self.env.ref('hr_holidays_notification.email_template_leave_for_approve')
            template_id.send_mail(res.id, force_send=True)
        return res


    @api.multi
    def action_validate(self):
        res = super(HrHolidays, self).action_validate()
        template_id = self.env.ref('hr_holidays_notification.email_template_leave_approve')
        template_id.send_mail(self.id, force_send=True)
        return res

    @api.one
    def action_refuse(self):
        record_id = self.id
        res=super(HrHolidays, self).action_refuse()
        template_id = self.env.ref('hr_holidays_notification.email_template_leave_rejection')
        template_id.send_mail(record_id, force_send=True)
        return True

