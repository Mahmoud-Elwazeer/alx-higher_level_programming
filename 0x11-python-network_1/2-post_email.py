#!/usr/bin/python3
""""import libraries"""
import urllib.request
import sys


def main():
    """main function"""
    url = sys.argv[1]
    add_email = sys.argv[2]
    req = urllib.request.Request(url)
    req.add_header('email', add_email)

    with urllib.request.urlopen(req) as response:
        get_header = response.getheader('email').decode('utf-8')
        print(f"Your email is: {get_header}")


if __name__ == "__main__":
    main()
