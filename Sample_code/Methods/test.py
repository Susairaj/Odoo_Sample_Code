# import os
# 
# x='workspace'
# y='file_name'
# path_1=os.path.abspath("Luna ifensys workspace\IFenSys\CricketsCrush-addons\cricketscrush\static\src\image")
# print(path_1)
# a= 2.00
# b= 30.30
# print a*b
#####################
# a= ['True','False']
# b = ['False','False']
# if 'True' in a:
#     print 'ok'
# if 'True' in b:
#     print 'no'
#########################
# a=[1, 2, 3, 4]
# b=[3, 4] 
# s1= set(a)
# s2 = set(b)
# s = list(s1-s2)
# print s
###############
# a = 'Act'
# l = a.lower()
# print l
# 
# import datetime
# 
# d_frm_obj = datetime.datetime.strptime('25-10-2016', DEFAULT_SERVER_DATETIME_FORMAT)
# d_to_obj = datetime.datetime.strptime('26-10-2016', DEFAULT_SERVER_DATETIME_FORMAT)
# 
# diff = d_to_obj - d_frm_obj
# 
# hours = (diff.seconds)/ 3600
# print hours
# 
# diff_days = diff.days
# print diff_days
# 
# days_hours = diff_days * 24
# print days_hours
# 
# total_hours = days_hours + hours
# print total_hours

# import time
# start_time = time.time()
# a= 1477413953.44
# b=1477413953.48
# print a/60
# print time.time()
# print("--- %s seconds ---" % (time.time() - start_time))

# import time
# from datetime import timedelta
# start_time = time.mktime(tuple)
# end_time = time.monotonic()
# print(timedelta(seconds=end_time - start_time))
# a = ['01:30', '06.45', '02.12', '06:57', '12:30', '00:30','01:30', '06.45', '02.12', '06:57', '12:30', '00:30','01:30', '06.45', '02.00', '06:57', '12:30', '00:30', '12:30'
#      , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30' , '12:30']
# min_count = 0
# sec_count = 0
# for b in a:
#     min_count = min_count + int(b[:2])
#     sec_count = sec_count + int(b[3:])
# # print min_count
# # print sec_count/60
# # print sec_count%60
# import yaml
# total_hrs = min_count + sec_count/60
# modulas = sec_count % 60
# print str(total_hrs) +':'+ str(modulas)
# m = str(total_hrs) +'.'+ str(modulas)
# x= float(m)
# z= yaml.load(m)
# hours = "%.2f" % (z)
# print hours
#######################################################
a =  [[0, False, {u'date': u'2016-10-01', u'place': False, u'type_id': 4}],
 [0, False, {u'date': u'2016-11-01', u'place': False, u'type_id': 5}]]
for b in a:
    if b[2]['type_id'] == 4:
        print b[2]['date']
        
#####################################
