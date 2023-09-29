#!/usr/bin/python3
"""
ists the 10 most recent
commits on a given GitHub repository.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[1], argv[2]
    )
    r = requests.get(url)
    cmmt = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                cmmt[i].get("sha"),
                cmmt[i].get("commit").get("author").get("name")
            ))
    except IndexError:
        pass
