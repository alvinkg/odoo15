# odoo15
Working on my Odoo cookbook
Odoo 15 Chapter 16 Remote Procedure Calls (RPC)
Creating/updating/deleting records through JSON-RPC

# create/update/delete records
(odoo-15-env) alvinlim@coolhandsg-iMac odoo15 % 
python3 jsonrpc_operation.py
user id: 2
Books created: {'jsonrpc': '2.0', 'id': 393724004, 'result': [22, 23, 24, 25]}
Books written: {'jsonrpc': '2.0', 'id': 266888396, 'result': True}
Books deleted: {'jsonrpc': '2.0', 'id': 551690682, 'result': True}

# Access Rights
(odoo-15-env) alvinlim@coolhandsg-iMac odoo15 % 
python3 jsonrpc_access_rights.py
2
 Has create access: True