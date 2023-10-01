#!/usr/bin/python3
"""import libraries"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def main():
    """main func"""
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))


if __name__ == "__main__":
    main()
