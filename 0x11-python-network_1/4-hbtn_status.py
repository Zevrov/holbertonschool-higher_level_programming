#!/usr/bin/python3
"""url fetching script in python"""

import requests

url = 'https://intranet.hbtn.io/status'


if __name__ == '__main__':
    req = requests.get(url)
    response = response.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
