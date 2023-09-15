from odoo import models,fields


class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'this is school student course'
    name = fields.Char()