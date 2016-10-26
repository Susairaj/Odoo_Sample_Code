from datetime import datetime
from dateutil.relativedelta import relativedelta
 
# number = [1,2,3,4];
# count= 0;
# for num in number:
#     count +=1
#     if not count > len(number):
#         date_after_month = datetime.today()+ relativedelta(months=count)
#         print 'Today: ',datetime.today().strftime('%d/%m/%Y')
#         print 'After Month:', date_after_month.strftime('%d/%m/%Y')

a=['2016-09-29', '2016-09-30', '2016-10-01', '2016-10-02', '2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06']
b = ['2016-09-29', '2016-09-30', '2016-10-04', '2016-10-05', '2016-10-06']
te_list = []
for d in a:
    if d in b:
        te_list.append(d)
    else:
        if not te_list ==[]:
            print min(te_list)
            print max(te_list)
            te_list = []
print min(te_list)
print max(te_list)
        