#!/usr/bin/python3
"""send a post request to a url, show response after"""

import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1],
                                b'email=' + sys.argv[2].encode()) as req:
                                    print(req.read().decode('UTF-8'))
