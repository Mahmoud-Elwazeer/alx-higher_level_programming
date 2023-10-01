#!/usr/bin/python3
""""import libraries"""
import requests
import sys


def main():
    """main function"""
    url = sys.argv[1]
    try:
        response = requests.get(url)
        code = response.status_code
        response.raise_for_status()
        content = response.content.decode('utf-8')
        print(content)

    except requests.exceptions.HTTPError as e:
        print(f"Error code: {code}")


if __name__ == "__main__":
    main()
