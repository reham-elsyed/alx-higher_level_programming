#!/usr/bin/python3
""" Method to fetch website"""
import urlib.request


if __name__ == '__main__':
    import urlib.request
    with urlib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".fortmat(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
