#-*- utf-8 -*-
from openerp import models, fields, api, exceptions
from datetime import datetime


class HrMission(models.Model):
    _name = 'hr.mission'
    _description = 'Mission object'

    employee_id = fields.Many2one('hr.employee', string='Employee', ondelete='cascade', required=True)
    mission_id = fields.Char(string='Mission ID', size=20, required=True)
    name = fields.Char(string='Mission Object', size=80, required=True)
    mission_objective = fields.Text(string='Objective')
    mission_start_date = fields.Datetime(string="Start date", required=True)
    mission_end_date = fields.Datetime(string="End date", required=True)
    mission_partner = fields.Many2one('res.partner', string='Mission partner', required=True)
    mission_location = fields.Char(string='Partner mission location')
    mission_partner_manager = fields.Many2one('res.partner', string='Partner mission manager', required=True)
    mission_duration = fields.Char(compute='_get_duration', default=0, string="Duration", readonly=True)
    mission_evaluation = fields.Text(string='Evaluation')
    mission_notes = fields.Text(string='Notes')
    mission_car = fields.Selection([('pc', 'Personal car'), ('cc', 'Common car'),
                                    ('plane', 'Plane'), ('boat', 'Boat'),
                                    ('other', 'Other')], string="Locomotion")
    mission_type = fields.Many2one('hr.mission.type', string='Mission Type', required=False)

    @api.constrains('mission_end_date')
    @api.onchange('mission_start_date', 'mission_end_date')
    def _get_duration(self):
        for rec in self:
            if rec.mission_start_date and rec.mission_end_date:
                if rec.mission_end_date > rec.mission_start_date:
                    time1 = datetime.strptime(rec.mission_start_date, "%Y-%m-%d %H:%M:%S")
                    time2 = datetime.strptime(rec.mission_end_date, "%Y-%m-%d %H:%M:%S")
                    delta = str(time2 - time1)
                    rec.mission_duration = delta
                else:
                    raise exceptions.ValidationError("Your mission end date must be higher than"
                                                     " mission start date ! %s" % rec.mission_end_date)


class HrEmployee(models.Model):
    _name = "hr.employee"
    _description = "Employee Category"
    _inherit = "hr.employee"

    in_mission = fields.Boolean(string="In Mission")
    missions_ids = fields.One2many('hr.mission', 'employee_id', string='Missions')


class HrExpense(models.Model):
    _name = 'hr.expense.expense'
    _description = "Expense"
    _inherit = 'hr.expense.expense'

    mission_id = fields.Many2one('hr.mission', 'Missions ID', help='Related mission if exist')


class HrMissionType(models.Model):
    _name = "hr.mission.type"
    _description = "Mission Type"

    name = fields.Char('Name', Required=True)
    description = fields.Text('Description', help='Describe this mission type aim !')
