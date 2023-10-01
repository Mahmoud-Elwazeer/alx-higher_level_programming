#!/usr/bin/python3
""""import libraries"""
import requests
import sys


def main():
    """main function"""
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    req_post = requests.post(url, data=values)
    # response = requests.get(url)
    content = req_post.content.decode('utf-8')

    print(content)


if __name__ == "__main__":
    main()
