# odoo15
Working on my Odoo cookbook
Odoo 15
Remote Procedure Calls in Odoo

1. Logging in to/connecting Odoo with XML-RPC
Outcome is success!
o15 % python3 books_data.py
Books ids found: [2, 3]
Books data: [{'id': 2, 'name': 'Odoo CookBook', 'date_release': '2022-11-24'}, {'id': 3, 'name': 'SQL for dummies like you', 'date_release': '2022-11-24'}]

We use two methods search and read in this exercise.
Search returns book ids, while read passes book data to the var Books_data.
I had to change the constants db_name to match.
The second exercise is with the mtd search read.  Much faster.
(odoo-15-env) alvinlim@coolhandsg-iMac odoo15 % python3 books_data2.py
Books data: [{'id': 2, 'name': 'Odoo CookBook', 'date_release': '2022-11-24'}, {'id': 3, 'name': 'SQL for dummies like you', 'date_release': '2022-11-24'}]