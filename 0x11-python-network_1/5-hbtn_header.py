#!/usr/bin/python3
"""script to return header from a url"""

import requests
import sys


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
