import urllib2

test = urllib2.urlopen('http://google.com', timeout=1)
print test
