# odoo15
Working on my Odoo cookbook

Creating interactive kanban cards
spent a bit of time troubleshooting why crash when using dropdown menu on kanban card: finally found the hypen is required!  
<div class="dropdown-menu" role="menu">

Adding a progress bar in kanban views
I did not try to link the sum_field attribute to calc other float/integer fields.

Using Python code server actions
Server actions based on python can allow advanced business rules without the need to create addon modules.
After creating the server actions it is required to upgrade the project module.

Enabling the archive option for records
This is quite simple really.

Adding a stat button to a form view
This is working but I am not quite clear how the action works.
I have to look at the Odoo Mates example later to get more info.

Creating QWeb-based PDF reports
The unanswered question is how to add the headers and footers for the external doc layout.

Managing activities from a kanban card
Quite straightforward.

Consuming parameters passed to your handlers
    # this is not working
    @http.route("/my_library/book_details/<model('library.book'):book>", type='http', auth='none')
    def book_details_in_path(self, book):
        return self.book_details(book.id)

For Chp 14
Odoo 15 no longer uses the views/templates.xml to indicate location of the scss, css, and js files.  Instead their paths are directly in the manifest.py file.  In the manifest.py...
    'assets': {
        'web.assets_frontend': [          
            'my_library/static/src/scss/my_library.scss',
            'my_library/static/src/css/my_library.css',
            'my_library/static/src/js/my_library.js',
            ],
    },
However I was not able to get the js file to work. until I removed the myodoo.define and replaced with just 'odoo.define(...)'

// myodoo.define('my_library', function(require){
//     var core = require('web.core');

//     alert(core._t('Hello World'));

//     return {
//         //if you created functionality to export, add it here.
//     }
// });
# this works!
odoo.define('my_library', function (require) {
    var core = require('web.core');

    alert(core._t('Hello world'));
    return {
        // if you created functionality to export, add it here
    }
});

I jumped to Chp 16 Owl because of the large changes to web dev in Odoo to Owl.
Creating an OWL component
1.  I do not use the template.xml in views dir.
2.  I used the manifest.py to add the component.js file to the assets_backend
3.  It seems to work, except the component was loaded on top instead of on the bottom.  Not sure why.