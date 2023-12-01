#!/usr/bin/python3
""" this is it """

import requests
import sys

if __name__ == "__main":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        reponse = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id", response.get("name"))))
    except ValueError:
        print("Not a valid JSON")
