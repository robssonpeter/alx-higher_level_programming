#!/usr/bin/python3
""" script to make a request using requests and sys"""


import requests
import sys

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as resp:
        print(resp.headers['X-Request-Id'])
