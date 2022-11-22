# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'my_library.my_library'

    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many(
        'res.partner',
        string = 'Authors'
    )

    category_id = fields.Many2one('library.book.category')    