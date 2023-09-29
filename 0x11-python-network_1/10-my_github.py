#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and password) and uses
the GitHub API to display your id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    user = argv[1]
    passowrd = argv[2]
    basic = HTTPBasicAuth(user, passowrd)
    r = requests.get("https://api.github.com/user", auth=basic)
    print(r.json().get("id"))
