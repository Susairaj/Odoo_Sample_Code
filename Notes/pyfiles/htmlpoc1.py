import html2text
h = html2text.HTML2Text()
h.ignore_links = True
print h.handle("<p>Hello<sup>3543</sup></p>")