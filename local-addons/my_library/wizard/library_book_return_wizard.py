# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LibraryBookReturnWizard(models.TransientModel):
    _name = 'library.return.wizard'
    _description = 'Library Book Return Wizard'
    
    borrower_id = fields.Many2one('res.partner', string='Borrower')
    # book_ids = fields.Many2many('library.book', string='Books')
    book_ids = fields.Many2many('library.book', string='Books', compute="onchange_member", readonly=False)
    
    def books_returns(self):
        loanModel = self.env['library.book.rent']
        for rec in self:
            loans = loanModel.search(
                [('state', '=', 'ongoing'),
                 ('book_id', 'in', rec.book_ids.ids),
                 ('borrower_id', '=', rec.borrower_id.id)]
            )
            for loan in loans:
                loan.book_return()
                
    @api.depends('borrower_id') 
    # @api.onchange('borrower_id')
    def onchange_member(self):
        rentModel = self.env['library.book.rent']
        books_on_rent = rentModel.search(
            [
                ('state','=','ongoing'),
                ('borrower_id','=',self.borrower_id.id)
            ]
        )
        self.book_ids = books_on_rent.mapped('book_id')
        
        # result = {
        #     'domain': {
        #         'book_ids': [('id', 'in', self.book_ids.ids)]
        #         }
        #     }
        # late_domain = [
        #         ('id', 'in', books_on_rent.ids),
        #         ('expected_return_date', '<', fields.Date.today())
        #     ]
        
        # late_books = loans.search(late_domain)
            
        # if late_books:
        #     message = ('Warn the member that the following books are late:\n')
        #     titles = late_books.mapped('book_id.name')
        #     result['warning'] = {
        #             'title': 'Late books',
        #             'message': message + '\n'.join(titles)
        #             }
        # return result