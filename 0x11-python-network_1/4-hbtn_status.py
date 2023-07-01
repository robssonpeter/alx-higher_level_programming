#!/usr/bin/python3
# python script to make a request using requests package


requests = __import__("requests")

url = "https://alx-intranet.hbtn.io/status"
with requests.get(url) as r:
    print("Body response:")
    print(f"\t - type: {type(r.text)}")
    print(f"\t - content: {r.text}")
