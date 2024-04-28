#!/usr/bin/python3
"""Script to sent data"""


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) < 2:
        payload = {'q': ''}
    else:
        payload = {'q': sys.argv[1]}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        r_js = r.json()
        if r.headers['content-type'] == 'application/json':
            if len(r_js) == 0:
                print("No result")
            else:
                print("[{}] {}".format(r_js.get('id'), r_js.get('name')))
        else:
            print("Not a Valid JSON")
    except ValueError:
        print("Not a Valid JSON")
