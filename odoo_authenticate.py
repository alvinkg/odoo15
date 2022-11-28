from xmlrpc import client

server_url = 'http://localhost:8069'
db_name = '15-3'
username = 'admin'
password = 'admin'

# below is the endpoint common
common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
user_id = common.authenticate(db_name, username, password, {})

if user_id:
    print("Success: User id is", user_id)
else:
    print("Failed: wrong credentials")