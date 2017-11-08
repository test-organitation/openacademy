# -*- coding: utf-8 -*-
from openerp import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(default=False, String="intructor patner")
    session_ids = fields.Many2many('openacademy.session', string="Session as attendee", readonly=True)
    test2 = fields.Char()
    test3 = fields.Char()
