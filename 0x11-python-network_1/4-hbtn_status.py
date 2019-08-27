#!/usr/bin/python3
"""url fetching script in python"""

import requests

url = 'https://intranet.hbtn.io/status'


if __name__ == '__main__':
    req = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
