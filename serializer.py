import json

def toJson(data):
    with open('./resources/data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
def fromJson(data):
    with open(data, 'r') as f:
        datastore = json.load(f)
        print (datastore)