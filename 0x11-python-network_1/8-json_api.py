#!/usr/bin/python3
""" import libraries """
import requests
import sys


def main():
    """main func"""
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}

    req = requests.post(url, data=values)
    try:
        json_response = req.json()
        print(f"[{json_response['id']}] {json_response['name']}")
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
