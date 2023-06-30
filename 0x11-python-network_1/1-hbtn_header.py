#!/usr/bin/python3
""" The script to read the header of the response """


from urllib import request
from sys import argv

if len(argv) > 1:
    with request.urlopen(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
