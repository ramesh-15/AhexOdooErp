from odoo import api,fields,models

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description ='this is school subjects'

    #fileds
    name = fields.Char("name", required=True)
    code = fields.Char("code", required=True)
    type = fields.Selection([
        ('compulsory','Compulsory'),
        ('optional', 'Optional'),])
    language = fields.Selection([
        ('english','English'),
        ('hindi', 'Hindi'),
        ('tamil', 'Tamil'),
        ('urdu', 'Urdu'),
        ('telugu', 'Telugu'),])
    credits = fields.Integer()