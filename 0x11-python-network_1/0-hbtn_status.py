#!/usr/bin/python3
""""import libraries"""
import urllib.request


def main():
    """main function"""
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf_content = content.decode('utf-8')
        print("Body response:")
        print(f"    - type: {type(content)}")
        print(f"    - content: {content}")
        print(f"    - utf8 content: {utf_content}")


if __name__ == "__main__":
    main()
