#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    load from json
    """
    with open(filename, 'r') as myfile:
        my_obj = json.loads(myfile.read())

    myfile.closed
    return (my_obj)
