#!/usr/bin/python3
""" The script to fetch from alx status page"""
from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    data = response.read()
print("Body response:$")
print(f"\t- type: {type(data)}$")
print(f"\t- content: {data}$")
print(f"\t- utf8 content {data.decode('utf-8')}$")
