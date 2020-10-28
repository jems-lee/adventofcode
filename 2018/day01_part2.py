import csv

FILENAME = 'input.csv'

with open(FILENAME, 'r') as f:
    reader = csv.reader(f)
    as_list = list(reader)

    last_index = len(as_list) - 1
    observed = set([0])
    total = 0
    counter = 0

    while True:
        new_freq = int(as_list[counter][0])
        total += new_freq
        if total in observed:
            print('repeated freq found: ', total)
            print('counter: ', counter)
            break
        else:
            observed.add(total)
        counter += 1
        if counter > last_index:
            counter = 0
