from BeautifulSoup import BeautifulSoup

raw = 'http://www.cricketscrush.com/shop-store/getall_products.php'
VALS = []
soup = BeautifulSoup(raw)

for x in soup.findAll("html:td"):
   if x.string == "Equity share capital":
       VALS = [y.string for y in x.parent.findAll() if y.has_key("class")]

print VALS