import json

def toJson(data):
    with open('./resources/data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)