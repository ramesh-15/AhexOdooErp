from odoo import models,fields,api

class Student(models.Model):
    _name = 'school.student'
    _description = 'this is school admission'


    @api.depends('course','grade')
    def _compute_fee(self):
        for record in self:
            if ((record.course == 'cbsc') or (record.course == 'ssc')) and record.grade =="ULK":
                record.fee = 250000
            elif ((record.course == 'cbsc') or (record.course == 'ssc')) and record.grade =="1":
                record.fee = 30000
            elif ((record.course == 'cbsc') or (record.course == 'ssc')) and ((record.grade =="2") or (record.grade =="3")):
                record.fee = 35000
            elif ((record.course == 'cbsc') or (record.course == 'ssc')) and ((record.grade =="5") or (record.grade =="4")):
                record.fee = 50000
            elif ((record.course == 'cbsc') or (record.course == 'ssc')) and ((record.grade =="6") or (record.grade =="7") or (record.grade =="8")):
                record.fee = 60000
            elif ((record.course == 'cbsc') or (record.course == 'ssc')) and ((record.grade =="9") or (record.grade =="10")):
                record.fee = 90000
            elif record.course == 'cbsc' and record.grade =="11":
                record.fee = 100000
            elif record.course == 'cbsc' and record.grade =="12":
                record.fee = 110000
            else:
                record.fee = 20000

    @api.onchange('track_id')
    def onchange_track_id(self):
        pass

    @api.onchange('gender')
    def onchange_gender(self):
        domain = [('desc', '!=', False)]
        if self.gender == 'f':
            domain = []
        # if gender = male there is no filter "view all tracks"
        return {
            'domain': {'track_id':domain}
        }

    name = fields.Char(required=True)
    rollid = fields.Char(required=True)
    age = fields.Integer()
    email = fields.Char()
    image = fields.Binary()
    gender = fields.Selection([
        ('m','Male'),
        ('f','Female'),
    ])
    course = fields.Selection([
        ('cbsc', 'CBSC'),
        ('ssc', 'SSC'),
    ])
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
    desc = fields.Text()
    join_date = fields.Datetime()
    date_of_birth = fields.Date()
    is_accepted = fields.Boolean()
    # course_line_ids = fields.One2many('school.course.line', 'student_id')
    fee = fields.Float(compute=_compute_fee, store=True)

    @api.depends('fee', 'payment')
    def _compute_due_fee(self):
        for record in self:
            # Calculate the due fee as the difference between the total fee and the payment made
            record.due_fee = record.fee - record.payment

    due_fee = fields.Float(compute=_compute_due_fee, store=True)
    payment = fields.Integer()
    track_id = fields.Many2one('school.track',string='Student Track')
    track_desc = fields.Text(related='track_id.desc',store=True,readonly=True)
    skill_ids = fields.Many2many('school.skill')
    state = fields.Selection([
        ('apply','Applied'),
        ('iq', 'Passed IQ'),
        ('tech', 'Passed Technical'),
        ('refused', 'Refused'),
        ('accepted', 'Accepted'),
    ],default='apply')

    def change_state(self):
        newstate = self.env.context['state']
        self.state = newstate

    def pass_tech(self):
        self.state = 'tech'

