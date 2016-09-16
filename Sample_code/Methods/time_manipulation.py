import datetime
import time

# print 'Times:'
# t1 = datetime.time(12, 55, 0)
# print '\tt1:', t1
# t2 = datetime.time(13, 5, 0)
# print '\tt2:', t2
# print '\tt1 < t2:', t1 < t2
# print '\tt1 - t2:', t1 - t2
# 
# print 'Dates:'
# d1 = datetime.date.today()
# print '\td1:', d1
# d2 = datetime.date.today() + datetime.timedelta(days=1)
# print '\td2:', d2
# print '\td1 > d2:', d1 > d2
from datetime import datetime
s1 = '00:30:00'
s2 = '00:59:00' # for example
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print tdelta