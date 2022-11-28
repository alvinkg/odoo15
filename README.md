# odoo15
Working on my Odoo cookbook
Odoo 15 Chapter 16 Remote Procedure Calls (RPC)
Fetching/searching records through JSON-RPC

(odoo-15-env) alvinlim@coolhandsg-iMac odoo15 % python3 json_fetch_data.py
# Search Method
payload = get_json_payload("object", "execute_kw",
        db_name, user_id, password,
        'library.book', 'search', [search_domain], {'limit': 5})

The execute_kw() method usually takes mandatory arguments as positional arguments, and optional arguments as keyword arguments. In the search method, domain is a mandatory argument, so we passed it in the list and passed the optional argument limit as the keyword argument (dictionary).

Search Result: {'jsonrpc': '2.0', 'id': 776243296, 'result': [2, 3]}
# Read Method
Books data: {'jsonrpc': '2.0', 'id': 226112554, 'result': [{'id': 2, 'name': 'Odoo CookBook', 'date_release': '2022-11-24'}, {'id': 3, 'name': 'SQL for dummies like you', 'date_release': '2022-11-24'}]}

# Search and Read Mtd
(odoo-15-env) alvinlim@coolhandsg-iMac odoo15 % python3 json_fetch_data2.py
Books data: {'jsonrpc': '2.0', 'id': 99403618, 'result': [{'id': 2, 'name': 'Odoo CookBook', 'date_release': '2022-11-24'}, {'id': 3, 'name': 'SQL for dummies like you', 'date_release': '2022-11-24'}]}