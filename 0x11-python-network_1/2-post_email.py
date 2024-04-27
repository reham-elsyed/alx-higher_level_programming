#!/usr/bin/python3
""" Method to take url and email and sends post request to the passed url"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(mail).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
