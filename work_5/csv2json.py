import csv
import json
from collections import defaultdict

columns = defaultdict(list)

with open(r'in.txt') as f:
    dataset = csv.DictReader(f)
    for row in dataset:
        for k, v in row.items():
            columns[k].append(int(v))


with open(r'out.txt', 'w') as j_file:
    json.dump(columns, j_file, indent=4, sort_keys=True)
