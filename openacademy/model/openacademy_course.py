from openerp import models, fields, api

'''
This module is to create model of Course
'''


class Course(models.Model):
    '''
    This class create model of Course
    '''
    _name = 'openacademy.course' # model odoo course

    name = fields.Char(string='Title', required='True') # Fileds reserved to identified name rec
    description = fields.Text(string='Description', required='False')

