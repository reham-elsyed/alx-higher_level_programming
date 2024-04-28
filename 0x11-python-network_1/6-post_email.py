#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    mail = sys.argv[2]
    requests.get(url)
    res = requests.post(url, data={'email': mail})
    print(res.text)
