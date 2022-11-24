# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError
from odoo.tools.translate import _
import logging

class LibraryBookRent(models.Model):
    _name = 'library.book.rent'
    _description = ''
    
    book_id = fields.Many2one('library.book', 'Book', required=True)
    borrower_id = fields.Many2one('res.partner', 'Borrower', required=True)
    state = fields.Selection(
        [
            ('ongoing','Ongoing'),
            ('returned','Returned'),
        ],
    'State',
    default='ongoing',
    required=True,
    )
    rent_date = fields.Date(default=fields.Date.today)
    return_date = fields.Date()
    
    @api.model
    def create(self, vals):
        book_rec = self.env['library.book'].browse(vals['book_id'])
        book_rec.make_borrowed()
        return super(LibraryBookRent, self).create(vals)
    
    def book_return(self):
        self.ensure_one()
        self.book_id.make_available()
        self.write({
            'state': 'returned',
            'return_date': fields.Date.today()
        })

