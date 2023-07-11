#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
script that adds all arguments to a Python list, and then save them to a file
"""

filesave = "add_item.json"
list_input = []
save_to_json_file(list_input, filesave)
list_input = load_from_json_file(filesave)
result = list_input + list(sys.argv[1:])
save_to_json_file(result, filesave)
