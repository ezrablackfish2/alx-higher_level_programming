#!/usr/bin/python3


from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print("Error code: ", e.code)
    except URLError as e:
        print("Error code: ", e.code)
    else:
        print(req.read())
