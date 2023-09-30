#!/usr/bin/python3
""""import libraries"""
import urllib.request
import sys


def main():
    """main function"""
    url = sys.argv[1]
    add_email = sys.argv[2]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        req.add_header('email', add_email)
        print(f"Your email is: {add_email}")


if __name__ == "__main__":
    main()
