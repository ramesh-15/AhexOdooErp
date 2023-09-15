from odoo import api,models, fields

class AttendanceEmployee(models.Model):
    _name = 'attendance.employee'
    _description ='this is employee'
    name = fields.Char("Name",required=True)