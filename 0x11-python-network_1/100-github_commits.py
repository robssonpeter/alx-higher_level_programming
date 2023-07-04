#!/usr/bin/python3
""" script to retrieve github commits """


import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    with requests.get(url) as resp:
        result = resp.json()
        if len(result) > 10:
            length = 10
        else:
            length = len(result)

        for n in range(length):
            name = result[n]['commit']['author']['name']
            print(f"{result[n]['sha']}: {name}")
