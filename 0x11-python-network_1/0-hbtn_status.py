#!/usr/bin/python3
""""import libraries"""
import urllib.request


def main():
    """main function"""
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        content = response.read()
        utf_content = content.decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {utf_content}")


if __name__ == "__main__":
    main()
