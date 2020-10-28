import csv

with open('input.csv', 'r') as f:
    reader = csv.reader(f)
    total = 0
    for row in reader:
        total += int(row[0])

print(total)
