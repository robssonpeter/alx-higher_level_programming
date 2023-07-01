#!/usr/bin/python3
# python script to make a request using requests package


import requests

url = "https://alx-intranet.hbtn.io/status"
r = requests.get(url)
print(f"\t - type: {type(r.text)}")
print(f"\t - content: {r.text}")
