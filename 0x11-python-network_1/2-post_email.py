#!/usr/bin/python3
""""import libraries"""
import urllib.request
import urllib.parse
import sys


def main():
    """main function"""
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)


if __name__ == "__main__":
    main()
