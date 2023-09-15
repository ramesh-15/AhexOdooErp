from odoo import api,fields,models

class Schoolfee(models.Model):
    _name = 'school.fee'
    _description ='this is school fee'

    def _compute_fee(self):
        for record in self:
            print(record)




    rollid=fields.Char("Roll Number", required=True)