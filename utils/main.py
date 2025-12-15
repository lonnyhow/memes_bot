import json


def read_json(filepath):
    with open(filepath, mode='r', encoding='utf-8') as file:
        return json.load(file)
