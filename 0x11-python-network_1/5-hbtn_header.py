#!/usr/bin/python3
"""Sript to get url ans print id"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
