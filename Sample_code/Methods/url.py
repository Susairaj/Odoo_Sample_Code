# from BeautifulSoup import BeautifulSoup
# import urllib2
# import re
# 
# html_page = urllib2.urlopen("http://www.cricketscrush.com/shop-store/getall_products.php")
# soup = BeautifulSoup(html_page)
# print soup
# for link in soup.findAll(attrs={'href': re.compile("^http://")}):
#     print link.get('href')
# import urllib
# import lxml.html
# connection = urllib.urlopen('http://www.cricketscrush.com/shop-store/getall_products.php')
# 
# dom =  lxml.html.fromstring(connection.read())
# print dom
# 
# for link in dom.xpath('//http://'): # select the url in href for all a tags(links)
#     print link
import urllib2
from bs4 import BeautifulSoup
url = 'http://www.cricketscrush.com/shop-store/getall_products.php'

conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html)
links = soup.find_all('tr')
ttt = soup.find_all('td')
for tname in ttt:
    print tname
# print ttt
# for tag in links:
#     link = tag.get('href',None)
#     if link is not None:
#         print link