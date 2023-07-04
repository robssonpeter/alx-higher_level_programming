#!/usr/bin/python3
""" Script for querying credentials on github """

import requests
import sys

url = "https://api.github.com/user"
user = sys.argv[1]
paswd = sys.argv[2]
headers = {
    "Authorization": f"Bearer {paswd}",
    "X-GitHub-Api-Version": "2022-11-28"
}
with requests.get(url, auth=(user, paswd), headers=headers) as resp:
    print(resp.json()['id'])
