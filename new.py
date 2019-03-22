import csv

print('_' * 100)
d = {}

with open('data.txt') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

print('_' * 100)
