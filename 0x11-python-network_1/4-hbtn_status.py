#!/usr/bin/python3
"""Python script to det url statue"""


if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
