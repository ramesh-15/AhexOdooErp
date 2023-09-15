from odoo import api, fields, models

class AhexEmployee(models.Model):
    _name = 'ahex.employee'
    _description ='Employees records...'
    # Other model attributes and methods here
    name = fields.Char(string="employee name" , required=True)
    address = fields.Char(string="employee Address", required=True)
    gender = fields.Selection([('Male',"Male"),("Female",'Female'),("Others","Others")],string='Gender')
    age = fields.Integer()

class AhexContractEmployee(models.Model):
    _name = 'ahex.contractemployee'
    _description = 'Contract Employee Records...'
    name = fields.Char(string='  Name',required=True)
    address = fields.Char(string='  Address',required=True)
    phone = fields.Char(string='  Phone Number')
    gender = fields.Selection([("Male","Male"),("Female","Female"),("others","others")],string='Gender')

class AhexFreelancerEmployee(models.Model):
    _name = 'ahex.freelanceremployee'
    _description = 'freelancer Employee Records...'
    name = fields.Char(string='  Name',required=True)
    address = fields.Char(string='  Address',required=True)
    phone = fields.Char(string='  Phone Number')
    gender = fields.Selection([("Male","Male"),("Female","Female"),("others","others")],string='Gender')