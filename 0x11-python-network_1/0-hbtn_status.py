#!/usr/bin/python3
""" this is america """

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()

print("type: {}".format(type(html)))
print("content: {}".format(html))
print("utf8 content: {}".format(html.decode("utf-8")))
