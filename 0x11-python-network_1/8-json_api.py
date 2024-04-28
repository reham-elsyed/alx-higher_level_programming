#!/usr/bin/python3
"""Send data to url"""


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) < 2:
        payload = {'q': ""}
    else:
        payload = {'q': sys.argv[1]}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    r_js = r.json()
    if r.headers['content-type'] is 'application/json':
        print("Not a Valid JSON")
    elif len(r_js) == 0:
        print("No result")
    else:
        print("[{}] {}".format(r_js.get('id'), r_js.get('name')))
    
