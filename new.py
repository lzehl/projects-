import csv

print('_' * 100)
d = {}

with open('data.txt') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
f.close()
print('_' * 100)
