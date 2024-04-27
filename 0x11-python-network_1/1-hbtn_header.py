#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""


if __name__ == '__main__':
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(dict(res.headers).get("X-Request-Id"))
