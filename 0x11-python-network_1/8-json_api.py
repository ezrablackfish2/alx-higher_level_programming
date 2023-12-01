#!/usr/bin/python3
""" this is it """

import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        reponse = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response["id"], response["name"]))
    except ValueError:
        print("Not a valid JSON")
