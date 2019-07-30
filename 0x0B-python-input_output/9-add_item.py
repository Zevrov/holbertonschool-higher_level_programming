#!/usr/bin/python3
'''Module for saving to json'''

import json
import os.path
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file = "add_item.json"
json_list = []

if os.path.exists(file):
    json_list = load_from_json_file(file)

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, file)
