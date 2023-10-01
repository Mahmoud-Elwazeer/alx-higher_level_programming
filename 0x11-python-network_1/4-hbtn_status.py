#!/usr/bin/python3
""""import libraries"""
import requests


def main():
    """main function"""
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.content)}")
    print(f"\t- content: {response.content.decode('utf-8')}")


if __name__ == "__main__":
    main()
