#!/usr/bin/python3
"""send a post request to a url, show response after"""

import requests
import sys


if __name__ == '__main__':
    request = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(request.text)
