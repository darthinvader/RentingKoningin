import json
from pandas import json_normalize

def open_json(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(json.loads(line))
    return json_normalize(data)

data = open_json('houses.json')
for d in data['link']:
    print(d)
