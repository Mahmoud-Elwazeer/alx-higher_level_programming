#!/usr/bin/python3
"""import libraries"""
import requests
import sys


def main():
    """main func"""
    url = "https://alx-intranet.hbtn.io/status"
    if len(sys.argv) == 2:
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}

    req = requests.post(url, data=values)
    json_response = req.json()

    print(f"[{json_response["id"]}] {json_response["name"]}")


if __name__ == "__main__":
    main()
