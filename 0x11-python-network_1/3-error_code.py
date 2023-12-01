#!/usr/bin/python3


from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    try:
        with response = urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: ", e.code)
    except URLError as e:
        print("Error code: ", e.code)
