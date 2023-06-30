#!/usr/bin/python3
""" the script to take an email and pass to
parameters """

from urllib.request import Request
import urllib.parse
from sys import argv

if (len(argv) > 2):
    obj = {"email":argv[2]}
    data = urllib.parse.urlencode(obj).encode()
    request = Request(argv[1], data, method="POST")
    with request as response:
        print(response.read().decode('utf-8'))
