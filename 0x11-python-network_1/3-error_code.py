#!/usr/bin/python3
"""import libraries"""
import urllib.request
import urllib.error
import sys


def main():
    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)

        with urllib.request.urlopen(req) as response:
            content = response.read()
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
