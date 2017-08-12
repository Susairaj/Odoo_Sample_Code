import xmlrpclib

username = 'admin' #the user
pwd = 'tendercuts123'      #the password of the user
dbname = 'tendercuts_apidemo'    #the database

# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://erp.tendercuts.in/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://erp.tendercuts.in/xmlrpc/object')
result = sock.execute(dbname, uid, pwd, 'stock.quant', 'get_product_qty',
    ['read'], {'store_name': "Stock",'prduct_id':2})
# result1 = sock.execute(dbname, uid, pwd, 'stock.quant', 'get_product_categ_qty',
#     ['read'], {'store_name': "Stock",'categ_name':'Chicken'})
# result2 = sock.execute(dbname, uid, pwd, 'stock.quant', 'get_store_qty',
#     ['read'], {'store_name': "Stock"})
print result
# print result1
# print result2
