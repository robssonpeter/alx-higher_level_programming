#!/usr/bin/python3
""" Script for querying credentials on github """


import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    paswd = sys.argv[2]
    headers = {
        "Authorization": f"Bearer {paswd}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    with requests.get(url, auth=(user, paswd)) as resp:
        if resp.status_code == 200:
            print(resp.json()['id'])
        else:
            print(None)
