# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class BaseArchive(models.AbstractModel):
    _name = 'base.archive'
    _description = 'wysiwyg'
    
    active = fields.Boolean(default=True)
    
    def do_archive(self):
        for record in self:
            record.active = not record.active