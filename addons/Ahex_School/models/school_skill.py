from odoo import models, fields

class SchoolSkill(models.Model):
    _name = 'school.skill'
    _description = 'this is school student skill'
    name = fields.Char()