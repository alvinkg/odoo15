# odoo15
Working on my Odoo cookbook
Chp 22 Point of Sale 
Adding custom JavaScript/SCSS files

Just like other modules we have to add the css, scss and js files directly in the manifest.py file.  For POS we need to add a first layer of 'assets' befofe adding the pos assets as below.

    'assets': {
        'point_of_sale.assets': [
            "pos_demo/static/src/js/pos_demo.js",
            # "pos_demo/static/src/scss/pos_demo.scss",
            ],
    },

The first file is pos_demo.js.  Code below.
console.log('Point of Sale JavaScript loaded');
We have success.

# pos_demo.scss
.pos .pos-content {
    .price-tag {
        background: #00abcd;
        border-radius: 12px;
        <!-- width: 100%;
        right: 0;
        left: 0;
        top: 0; -->
    }
}
color of background is 100% width.