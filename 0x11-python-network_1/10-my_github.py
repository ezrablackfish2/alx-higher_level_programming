#!/usr/bin/python3
""" auth """

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    ourauth = (sys.argv[1], sys.argv[2])
    r = requests.get("http://api.github.com/user", auth=ourauth)
    res = r.json()
    print(res.get("id"))
