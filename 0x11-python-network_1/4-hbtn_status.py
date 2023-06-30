#!/usr/bin/python3
"""script to make  a request """


import urllib.requests

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    resp = response.read().decode('utf-8')

print("Body response:$")
print(f"\t- type: {type(resp)}$")
print(f"\t- type: {resp}$")
