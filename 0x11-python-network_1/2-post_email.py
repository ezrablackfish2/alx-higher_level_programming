#!/usr/bin/python3
""" wahahaha """

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    data = {}
    data["email"] = sys.argv[2]
    value = urllib.parse.urlencode(data).encode("ascii")

    url = sys.argv[1]
    req = urllib.request.Request(url, value)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    print(the_page.decode("utf-8"))
