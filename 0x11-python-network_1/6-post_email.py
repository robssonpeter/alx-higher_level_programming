#!/usr/bin/python3
""" Make a pos request passing an email in params """


import requests
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]
    params = {"email": email}
    with requests.post(url, params=params) as resp:
        print(resp.text)
