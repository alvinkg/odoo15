# odoo15
Working on my Odoo cookbook
Odoo 15
Remote Procedure Calls in Odoo

1. Logging in to/connecting Odoo with XML-RPC
(odoo-15-env) alvinlim@coolhandsg-iMac odoo15 % python3 odoo_authenticate.py
Success: User id is 2

We use the std python xmlrpc lib to access odoo instance.
Likewise, for the version_info.py success.
(odoo-15-env) alvinlim@coolhandsg-iMac odoo15 % python3 version_info.py
{'server_version': '15.0', 'server_version_info': [15, 0, 0, 'final', 0, ''], 'server_serie': '15.0', 'protocol_version': 1}