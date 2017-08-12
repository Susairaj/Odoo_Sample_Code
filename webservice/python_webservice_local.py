import xmlrpclib

username = 'admin' #the user
pwd = 'admin'      #the password of the user
dbname = 'tendercuts_new'    #the database

# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://localhost:8069/xmlrpc/common',allow_none=True)
uid = sock_common.login(dbname, username, pwd)

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object',allow_none=True)
result = sock.execute(dbname, uid, pwd, 'stock.quant', 'get_product_qty',
    ['read'], {'store_id': 15,'prduct_id':1})
print result
result1 = sock.execute(dbname, uid, pwd, 'stock.quant', 'get_product_categ_qty',
    ['read'], {'store_id': 15,'categ_name':'Chicken'})
print result1
result2 = sock.execute(dbname, uid, pwd, 'stock.quant', 'get_store_qty',
    ['read'], {'store_id': 15})
print result2
# Sale Creation
sale_order = sock.execute(dbname, uid, pwd, 'sale.order.api', 'create_sale_order',
     ['read'], {'partner_id': 1,'partner_name': "muthutest",'street':'Anna Salai','street2':'2nd cross','city':'Vellore','phone':'9876554421','email':'xxx@gmail.com','product_list':[{'product_id':1,'ordered_qty':1, 'unit_price':200},
                                                       {'product_id':1,'ordered_qty':2, 'unit_price':300}]})
print sale_order
invoice_order = sock.execute(dbname, uid, pwd, 'account.invoice.api', 'invoice_creation',
    ['read'], {'partner_name': "muthutest",'street':'Anna Salai','street2':'2nd cross','city':'Vellore','phone':'9876554421','email':'xxx@gmail.com',
               'product_list':[{'product_id':1,'ordered_qty':1, 'unit_price':200},
                               {'product_id':1,'ordered_qty':2, 'unit_price':300}]})
print invoice_order
# print result
# print result1
# print result2
