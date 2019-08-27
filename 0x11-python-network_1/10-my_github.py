#!/usr/bin/python3
"""script to get the id of an authenticated github user"""

import requests
import sys


if __name__ == "__main__":
    search = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2])
    )
    print(search.json().get("id"))
