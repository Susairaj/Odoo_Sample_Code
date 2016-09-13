import os
file_list = []
a = 'CB-005'
for file in os.listdir("D:/image path/im1"):
    if file.endswith(".jpg"):
#         print file.rfind('_')
#         print file[:file.rfind('_')]
        if file[:file.rfind('_')] == 'CB-005':
            print 'ok'
            print file
#         print file
        file_list.append(file)
# print file_list
# for file in file_list:
    
