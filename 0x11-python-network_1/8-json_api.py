#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    let = "" if len(argv) == 1 else argv[1]
    search = {"q": let}

    r = requests.post("http://0.0.0.0:5000/search_user", data=search)

    try:
        rep = r.json()
        if rep == {}:
            print(" No result")
        else:
            print("[{}] {}".format(rep.get("id"), rep.get("name")))
    except ValueError:
        print("Not a valid JSON")
