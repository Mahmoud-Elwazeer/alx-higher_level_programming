#!/usr/bin/python3
""""import libraries"""
import requests
import sys


def main():
    """main function"""
    url = sys.argv[1]
    response = requests.get(url)
    get_header = response.headers.get('X-Request-Id')

    print(get_header)


if __name__ == "__main__":
    main()
