# odoo15
Working on my Odoo cookbook
Odoo 15 Chapter 16 Remote Procedure Calls (RPC)
API Keys

Odoo 15 requires that we use 2FA and have relocated the api keys under the account preferences/account security tab.  Developer mode should be activated.

# replacing pw with api key done!
(odoo-15-env) alvinlim@coolhandsg-iMac odoo15 % 
python3 jsonrpc_method.py
Book created with id: 32
Book state after the method call: [{'id': 32, 'name': 'Book 1', 'state': 'available'}]
