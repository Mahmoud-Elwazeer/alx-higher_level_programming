#!/usr/bin/python3
""""import libraries"""
import requests


def main():
    """main function"""
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.content.decode('utf-8')

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")


if __name__ == "__main__":
    main()
