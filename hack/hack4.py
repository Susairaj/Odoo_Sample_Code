import optparse

import requests

import re

parser = optparse.OptionParser()
parser.add_option('-t','–target', action="store", dest="hostname", help="host where you want to check for common files.", default="spam")
parser.add_option('-p', '–port', action="store", dest="port", help="Port number to be used while hitting the host", default="80")

#parser.add_option(‘-‘, ‘–search’, action=”store”, dest=”search”, help=”Define any search pattern, string / regex to be highlighted in the response pages.”, default=”spam”)

options, args = parser.parse_args()

hostregex = re.compile("^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$")

ipregex = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")

host = options.hostname

port = options.port

if hostregex.match(host):

    print "Checking clickjacking on %s:%s" % (host,port)

    if (port == 443):

        req = requests.get("https://"+ host)

    else:

        req = requests.get("http://" + host + ":" + port)

    try:

        print "[-] Not vulnerable to ClickJ\nX-Frame-Options response header present, Contains value %s\n" % (req.headers['X-Frame-Options'])

    except:

        print "[+] Vulnerable to ClickJacking, but check framebusting.\n"

elif ipregex.match(host):

    print "Checking clickjacking on %s:%s" % (host,port)

    if (port == 443):

        req = requests.get("https://" + host)

    else:

        req = requests.get("http://" + host + ":" + port)

    try:

        print "[-] Not vulnerable to ClickJ\nX-Frame-Options response header present, Contains value %s\n" % (req.headers['X-Frame-Options'])

    except:

        print "[+] Vulnerable to ClickJacking, but check framebusting.\n"

else:

    print "Please enter valid Hostname / IP Address"