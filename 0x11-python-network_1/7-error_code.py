#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
