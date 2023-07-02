#!/usr/bin/python3
""" the script to sent a query string for searching """


import requests
import sys

url = "http://0.0.0.0:5000/search_user"
if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    query = ""
parameters = {
    "q": query
}
with requests.post(url, data=parameters) as resp:
    json_resp = resp.json()
    if isinstance(json_resp, type({})):
        if len(json_resp.keys()):
            print(f"[{json_resp['id']}] {json_resp['name']}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
