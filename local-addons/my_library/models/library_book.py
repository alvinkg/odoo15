# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError
from odoo.tools.translate import _


class BaseArchive(models.AbstractModel):
    _name = 'base.archive'
    _description = 'Abstract Archive'

    active = fields.Boolean(default=True)

    def do_archive(self):
        for record in self:
            record.active = not record.active
            
class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'my_library.my_library'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'
    _inherit = ['base.archive']

        
    short_name = fields.Char('Short Title', translate=True, index=True)
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many(
        'res.partner',
        string = 'Authors'
    )


    notes = fields.Text('Internal Notes')
    state = fields.Selection(
        [
            ('draft','Not Available'),
            ('available','Available'),
            ('lost','Lost'),
        ],
        'State', default="draft") 

    description = fields.Html('Description', sanitize=True, strip_style=False)
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated', copy=False)
    pages = fields.Integer('Number of Pages',
        groups='base.group_user',
        states={'lost': [('readonly', True)]},
        help='Total book page count', company_dependent=False)
    reader_rating = fields.Float(
        'Reader Average Rating',
        digits=(14, 4),  # Optional precision (total, decimals),
    )
    author_ids = fields.Many2many('res.partner', string='Authors')
    cost_price = fields.Float('Book Cost', digits='Book Price')
    currency_id = fields.Many2one('res.currency', string='Currency')
    retail_price = fields.Monetary('Retail Price') # optional attribute: currency_field='currency_id' incase currency field have another name then 'currency_id'
    publisher_id = fields.Many2one('res.partner', string='Publisher',
        # optional:
        ondelete='set null',
        context={},
        domain=[],
    )
    publisher_city = fields.Char(
        'Publisher City',
        related='publisher_id.city',
        readonly=True
    )
    category_id = fields.Many2one('library.book.category')
    age_days = fields.Float(
        string='Days Since Release',
        compute='_compute_age',
        search='_search_age',
        store=False, # optional
        compute_sudo=True # optional
    )

    def name_get(self):
        """ This method used to customize display name of the record """
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_release)
            result.append((record.id, rec_name))
        return result

    # _sql_constraints = [
    #     ('name_uniq', 'UNIQUE (name)', 'Book title must be unique.'),
    #     ('positive_page', 'CHECK( pages > 0)', 'Number of pages must be greater than zero.')
    # ]
    
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'Book title must be unique.'),
        ('positive_page', 'CHECK(pages > 0)', 'No of pages must be positive')
    ]

    @api.constrains('date_release')
    def _check_release_date(self):
        for record in self:
            if record.date_release and record.date_release > fields.Date.today():
                raise models.ValidationError('Book release date must be in the past.')    
            
    # calc num of days from book date release
    @api.depends('date_release')
    def _compute_age(self):
        today = fields.Date.today()
        for book in self:
            if book.date_release:
                delta = today - book.date_release
                book.age_days = delta.days
            else:
                book.age_days = 0

    # to write on compute field
    def _inverse_age(self):
        today = fields.Date.today
        for book in self.filtered('date_release'):
            d = today - timedelta(days=book.age_days)
            book.date_release = d

    # to search compute fields
    def _search_age(self,operator, value):
        today = fields.Date.today()
        value_days = timedelta(days=value)
        value_date = today - value_days

        operator_map = {
            '>': '<', '>=':'<=',
            '<': '>', '<=': '>=',
        }

        new_op = operator_map.get(operator, operator)
        return [('date_release', new_op, value_date)]
    
    @api.model
    def _referencable_models(self):
        models = self.env['ir.model'].search([
            ('field_id.name', '=', 'message_ids')
        ])
        return [(x.model, x.name) for x in models]
    
    ref_doc_id = fields.Reference(
        selection='_referencable_models',
        string='Reference Document',
    )

    state = fields.Selection([
        ('draft', 'Unavailable'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')],
      'State', default='draft')
    
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        print(old_state, new_state)
        allowed = [('draft','available'),
            ('available','borrowed'),
            ('borrowed','available'),
            ('available','lost'),
            ('borrowed','lost'),
            ('lost','available')]
        return (old_state, new_state) in allowed
    
    def change_state(self, new_state):
        for book in self:
            print('inside for loop')
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                msg = _('Moving from %s to %s is not allowed.') % (book.state, new_state)
                raise UserError(msg)
    
    def make_available(self):
        self.change_state('available')
        print('make available')
        
    def make_borrowed(self):
        self.change_state('borrowed')
        print('make borrowed')
        
    def make_lost(self):
        self.change_state('lost')
        print('make lost')
        
        
    def log_all_library_members(self):
        # this is an empty recordset of model library.member
        library_member_model = self.env['library.member']
        all_members = library_member_model.search([])
        print("All Members:", all_members)
        return True
    
    
    def create_categories(self):
        categ1 = {
            'name': 'Child category 1',
            'description': 'Description for child 1'
        }
        categ2 = {
            'name': 'Child category 2',
            'description': 'Description for child 2'
        }
        parent_category_val = {
            'name': 'Parent category',
            'description': 'Description for parent category',
            'child_ids': [
                (0, 0, categ1),
                (0, 0, categ2),
            ]
        }
        # Total 3 records (1 parent and 2 child) will be craeted in library.book.category model
        record = self.env['library.book.category'].create(parent_category_val)
        return True    

    def change_release_date(self):
        self.ensure_one()
        self.date_release = fields.Date.today()
        # use the below commented code if there are more than one field to update
        # self.update({
        #     'date_release': fields.Datetime.now(),
        #     'another_field': 'value'
        # })
    
class ResPartner(models.Model):
    _inherit = 'res.partner'
    _order = 'name'

    published_book_ids = fields.One2many('library.book', 'publisher_id', string='Published Books')
    authored_book_ids = fields.Many2many(
        'library.book',
        string='Authored Books',
        # relation='library_book_res_partner_rel'  # optional
    )

    count_books = fields.Integer('Number of Authored Books',
                                compute='_compute_count_books')
    
    @api.depends('authored_book_ids')
    def _compute_count_books(self):
        for rec in self:
            rec.count_books = len(rec.authored_book_ids)