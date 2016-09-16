'''
Created on Jan 27, 2016

@author: bosco
'''
import sys, os

print 'sys.argv[0] =', sys.argv[0]
pathname = os.path.dirname(sys.argv[0])
print 'path =', pathname
print 'full path =', os.path.abspath(pathname)
