#!/usr/bin/python3
""" this is america """

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
print("Body response:$")
print("\t- type: {}$".format(type(html)))
print("\t- content: {}$".format(html))
print("\t- utf8 content: {}$".format(html.decode("utf-8")))
