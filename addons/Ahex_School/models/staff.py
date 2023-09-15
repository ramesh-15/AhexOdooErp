from odoo import api,models, fields

class SchoolStaff(models.Model):
    _name = 'school.staff'
    _description ='this is school staff'
    name = fields.Char(required=True)
    professional = fields.Char('professional', required=True)
    subject = fields.Char('subject', required=True)
    age = fields.Integer()
    experience = fields.Integer()
    email = fields.Char()
    image = fields.Binary()
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
    ])
    join_date = fields.Datetime()
    date_of_birth = fields.Date()
    salary = fields.Float()
    address = fields.Char('address')
