import pymysql
 
connection = pymysql.connect(host='139.162.51.169',
                      user='root',
                      password='!qazmlp)5',
                      db='odoo',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
 
cursor = connection.cursor()
 
# Selecting.
query = "SELECT * FROM `cataloginventory_stock_item` "
cursor.execute(query)
 
if cursor.rowcount == 0:
    print ('No results matched your query.')
else:
    print (cursor.fetchone()['item_id'])
    print (cursor.fetchall())
    
 
## Inserting
#query = "INSERT INTO `table` (id) VALUES (1)"
#cursor.execute(query)
# 
#connection.commit() # You need this if you want your changes 'commited' to the database.