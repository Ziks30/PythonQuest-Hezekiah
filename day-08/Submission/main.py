import csv
import json

with open('example1.csv', 'r') as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)

with open('example2.json', 'r') as file1:
    data = json.load(file1)

    out = json.dumps(data, indent=4)
    print(out)