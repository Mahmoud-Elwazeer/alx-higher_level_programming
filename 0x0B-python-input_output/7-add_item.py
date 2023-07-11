#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys


filesave = "add_item.json"
list_input = []
save_to_json_file(list_input, filesave)
list_input = load_from_json_file(filesave)
result = list_input + list(sys.argv[1:])
save_to_json_file(result, filesave)
