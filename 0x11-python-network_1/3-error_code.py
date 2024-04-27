#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays"""


if __name__ == "__main__":
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as res:
        print(res.read().decoded('utf-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
