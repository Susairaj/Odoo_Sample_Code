#import fnmatch
#import os
#import webbrowser
#song = raw_input("enter the song")
#to_search = [song + '.mp3']
#
#path = ['G:\\','F:\\','E:\\']
#for k in path:
#    for root, dirnames, filenames in os.walk(k):
#       for extensions in to_search:
#        for filename in fnmatch.filter(filenames, extensions):
#            matches=(os.path.join(root, filename))
#print matches
#if not matches:
#    print ("no such song is found")
#else:
#    webbrowser.open(matches)


#import os
#import glob
#newest = max(glob.iglob('*.[Mm][Pp]3'), key=os.path.getctime)

import os

def mp3gen():
    path = ['G:\\','F:\\','E:\\']
    for k in path:
        for root, dirs, files in os.walk(k):
            for filename in files:
                if os.path.splitext(filename)[1] == ".mp3":
                    yield os.path.join(root, filename)

for mp3file in mp3gen():
    print mp3file