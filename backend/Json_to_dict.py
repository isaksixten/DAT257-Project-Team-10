import json

def json_to_dict(file):
    with open(f'{file}', 'r', encoding='utf-8') as json_file:
        your_dict = json.load(json_file)
    return your_dict

