#!/usr/bin/python3
""" the script to show the error code """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as resp:
        if resp.status_code >= 400:
            print(f"Error code: {resp.status_code}")
        else:
            print(resp.text)
