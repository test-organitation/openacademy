# -*- coding: utf-8 -*-
from openerp import fields, models

class Parther(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many('openacademy.session', string="Session as intructor", readonly=True)
