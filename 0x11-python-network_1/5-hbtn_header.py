#!/usr/bin/python3
""" header content """

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    z = r.headers["X-Request-Id"]
    print(z)
