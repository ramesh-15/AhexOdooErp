from odoo import models,fields


class SchoolCourseLine(models.Model):
    _name = 'school.course.line'
    _description = 'this is school student course line'

    student_id = fields.Many2one('school.student')
    # student_course = fields.Many2one('school.student','name')
    course_id = fields.Many2one('school.course')

    grade = fields.Selection([
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),
        ('e','E'),
    ])