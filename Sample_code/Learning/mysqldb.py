#import MySQLdb                                    #1
#connection=MySQLdb.connect(host="staging.tendercuts.in", user="root", passwd="!qazmlp)5", db="odoo")  #2
#cur=connection.cursor()                           #3
##cur.execute("create table lfy(name varchar(40), author varchar(40))")  #4
##cur.execute("insert into lfy values('Foss Bytes','LFY Team')")         #5
##cur.execute("insert into lfy values('Connecting MySql','Ankur Aggarwal')")
#cur.execute("select * from aitoc_cataloginventory_stock_item")                  #6
#multiplerow=cur.fetchall()                        #7
#print   "Displaying All the Rows:", multiplerow
#print multiplerow[0]
#cur.execute("select * from lfy")
#row=cur.fetchone()                                #8
#print  "Displaying the first row: ", row
#print "No of rows: ", cur.rowcount                #9
#cur.close()                                       #10
#connection.close()                                #11

import pymysql
db = pymysql.connect(host='http://localhost/',user='admin',passwd='admin123')
cursor = db.cursor()
query = ("SHOW DATABASES")
cursor.execute(query)
for r in cursor:
    print r