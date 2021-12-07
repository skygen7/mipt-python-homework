import pickle
import json

with open('in', 'rb') as pick_f:
    data = pickle.load(pick_f)

with open('out.txt', 'w') as json_f:
    json.dump(data, json_f, indent=4, sort_keys=True)
