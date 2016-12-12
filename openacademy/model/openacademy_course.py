from openerp import models, fields

'''
This module is to create model of Course
'''


class Course(models.Model):
    '''
    This class create model of Course
    '''
    _name = 'openacademy.course' # model odoo course

    name = fields.Char(string='Title', required=True) # Fileds reserved to identified name rec
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one(
        'res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
       'openacademy.session', 'course_id', string="Sessions")
