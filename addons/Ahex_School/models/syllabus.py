from odoo import api,fields,models

class SchoolSyllabus(models.Model):
    _name = 'school.syllabus'
    _description ='this is school syllabus'
    #fields
    name= fields.Char('name',required = True)
    subject= fields.Char('subject',required = True)
    grade = fields.Selection([
        ('nursery', 'Nursery'),
        ('lkg', 'LKG'),
        ('ukg', 'UKG'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),

    ])
    duration= fields.Integer()