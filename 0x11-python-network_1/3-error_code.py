#!/usr/bin/python3
"""send a web req with error handling"""

import urllib.request
import sys


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
