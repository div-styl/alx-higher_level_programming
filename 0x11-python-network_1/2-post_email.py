#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
from urllib import parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    mail = {"email": argv[2]}
    alxurl = parse.urlencode(mail).encode("ascii")

    req = urllib.request.Request(url, alxurl)
    with urllib.request.urlopen(req) as reques:
        print(reques.read().encode("utf-8"))

