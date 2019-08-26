#!/usr/bin/python3
"""url fetching script in python"""

import urllib.request

url = 'https://intranet.hbtn.io/status'


with urllib.request.urlopen(url) as response:
    html = response.read()
    type_html = type(html)
    print("Body response:")
    print("\t- type: {}".format(type_html))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
