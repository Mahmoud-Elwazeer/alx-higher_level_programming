#!/usr/bin/python3
""""import libraries"""
import urllib.request
import sys


def main():
    """main function"""
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        get_header = response.getheader('X-Request-Id')
        print(get_header)


if __name__ == "__main__":
    main()
