#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
variable found in the header of the response.
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    alxurl = urllib.request.Request(argv[1])
    with urllib.request.urlopen(alxurl) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
