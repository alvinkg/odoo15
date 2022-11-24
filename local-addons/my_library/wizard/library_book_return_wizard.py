# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LibraryBookReturnWizard(models.TransientModel):
    _name = 'library.return.wizard'
    _description = 'Library Book Return Wizard'
    
    borrower_id = fields.Many2one('res.partner', string='Borrower')
    book_ids = fields.Many2many('library.book', string='Books')
    
    def books_returns(self):
        loanModel = self.env['library.book.rent']
        for rec in self:
            loans = loanModel.search(
                [('state', '=', 'ongoing'),
                 ('book_id', 'in', rec.book_ids.ids),
                 ('borrower_id', '=', rec.borrower_id.id)]
            )
            for loan in loans:
                print('inside loan')
                loan.book_return()
                print('loan returned')
                
                
    @api.onchange('borrower_id')
    def onchange_member(self):
        rentModel = self.env['library.book.rent']
        books_on_rent = rentModel.search(
            [
                ('state','=','ongoing'),
                ('borrower_id','=',self.borrower_id.id)
            ]
        )
        self.book_ids = books_on_rent.mapped('book_id')