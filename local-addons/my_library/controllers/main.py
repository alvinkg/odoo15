from odoo import http, fields
from odoo.http import request
# from odoo import fields
import email
import datetime


class Main(http.Controller):
    
    @http.route('/my_library/books', type='http', auth='none')
    def books(self):
        # create a var books and assign the results of a search of library.book
        books = request.env['library.book'].sudo().search([])
        # start assigning the construct of a webpage to the var below
        html_result = '<html><body><ul>'
        # assign a line to the name of each book found
        for book in books:
            html_result += "<li>%s</li>" % book.name
        html_result += '</ul></body></html>'
        return html_result
    
    # I was unable to get the dates either
    @http.route('/my_library/books2', type='http', auth='none')
    def books2(self):
        # create a var books and assign the results of a search of library.book
        books = request.env['library.book'].sudo().search([])
        html_result = '<html><body><ul>'
        
        for book in books:
            html_result += "<li>%s</li>" % book.name
        html_result += '</ul></body></html>'
        # return html_result
        return request.make_response(
            html_result, headers=[
                ('Last-modified', email.utils.formatdate(
                    (
                    fields.Datetime.from_string(request.env['library.book'].sudo().search([], order='write_date desc', limit=1).write_date)-datetime.datetime(1970, 1, 1)).total_seconds(), usegmt=True)),
                ])
        
    # does not work even with --db-filter='15-3'$ added as an option
    @http.route('/my_library/books/json', type='json', auth='none')
    def books_json(self):
        records = request.env['library.book'].sudo().search([])
        return records.read(['name'])
    
    @http.route('/my_library/all_books', type='http', auth='none')
    def all_books(self):
        # create a var books and assign the results of a search of library.book
        books = request.env['library.book'].sudo().search([])
        # start assigning the construct of a webpage to the var below
        html_result = '<html><body><ul>'
        # assign a line to the name of each book found
        for book in books:
            html_result += "<li>%s</li>" % book.name
        html_result += '</ul></body></html>'
        return html_result
    
    @http.route('/my_library/all_books/mark_mine', type='http', auth='public')
    def all_books_mark_mine(self):
        books = request.env['library.book'].sudo().search([])
        html_result = '<html><body><ul>'
        for book in books:
            if request.env.user.partner_id.id in book.author_ids.ids:
                html_result += "<li><b>%s</b></li>" % book.name
            else:
                html_result += "<li>%s</li>" % book.name
        html_result += '</ul></body></html>'
        return html_result
    
    @http.route('/my_library/all_books/mine', type='http', auth='user')
    def all_books_mine(self):
        
        books = request.env['library.book'].search([('author_ids','in', request.env.user.partner_id.ids)])
   
        html_result = '<html><body><ul>'
        for book in books:
            html_result += "<li>%s</li>" % book.name
        html_result += '</ul></body></html>'
        return html_result
    
    # @http.route('/my_library/book_details', type='http', auth='none')
    # def book_details(self, book_id): 
    #     record = request.env['library.book'].sudo().browse(int(book_id))
    #     return u'<html><body><h1>%s</h1>Authors: %s' % (record.name, u', '.join(record.author_ids.mapped('name')) or 'none',
    #         )

    # @http.route("/my_library/book_details_in_path/<model('library.book'):book>", type='http', auth='none')
    # def book_details_in_path(self, book): 
    #     return self.book_details(book.id)
    
    @http.route('/my_library/book_details', type='http', auth='none')
    def book_details(self, book_id):
        record = request.env['library.book'].sudo().browse(int(book_id))
        return u'<html><body><h1>%s</h1>Authors: %s' % (
            record.name,
            u', '.join(record.author_ids.mapped('name')) or 'none',
        )
    # this is not working
    @http.route("/my_library/book_details/<model('library.book'):book>", type='http', auth='none')
    def book_details_in_path(self, book):
        return self.book_details(book.id)