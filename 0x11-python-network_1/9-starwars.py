#!/usr/bin/python3
"""Module that sends a search req to Star Wars api"""

import requests
import sys


if __name__ == '__main__':
    search = requests.get(
        'https://swapi.co/api/people/',
        params={'search': sys.argv[1]}
    )
    response = search.json()
    print('Number of results:', response.get('count'))
    for thing in response.get('results'):
        print(thing.get('name'))
