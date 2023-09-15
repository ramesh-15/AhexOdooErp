from odoo import api, fields, models

class AhexDepartment(models.Model):
    _name = 'ahex.department'
    _description ='Department records...'
    # Other model attributes and methods here
    name = fields.Char(string="name" , required=True)
    code = fields.Char("Dept Code",required=True)
    address = fields.Char(string="Address", required=True)
