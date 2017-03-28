#a= {'product_id': 6, 'qty': 7.0}
#print a['product_id']
#a = []
#d = '280,280'
#m= d.split(',')
#for d1 in m:
#    print d1
#################
#a = [u'282']
#for b in a:
#    print type(int(b))
#    print b
########################
#a = [[0, False, {u'date_expected': False, u'avail_qty': u'6.0', u'product_uom': 20, u'location_dest_id': 34, u'product_qty': 0.11, u'procure_method': False, u'location_id': 15, u'product_id': 6}]]
#for b in a:
#    print b[2]['date_expected']

#a = (0, 0, {'sku_id': 6, 'barcode': u'1000010008736', 'serial_no_id': 1903})
#print a[2]['serial_no_id']

################
#d=[True,False]
#if False in d:
#    print 'yes'
#######################
#d=[]
#a = ['1000010005056\n1000010005162\n1000010005278']
#for m in a.split('\n'):
#    d.append(m)
#print d
#############
#a ='These are the products going to expire today!'
#print a.upper()

a= [[133, 1]]
count = 0
for b in a:
    count +=1
    print b[0]
    print b[1]+1