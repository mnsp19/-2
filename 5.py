import csv
import random

with open('scientist (1).txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    r = [i for i in range(1024)]
    random.shuffle(r)
    for s in reader:
        name = s['ScientistName']
        indexes = []
        code = 0
        for i in name:
            code += r[ord(i) % 1024]
        s['hash'] = str(code % 2048)

with open('scientist_with_hash.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, delimiter='#', fieldnames=['hash', 'ScientistName', 'preparation', 'date',
                                                             'components'])
    writer.writeheader()
    writer.writerows(reader)
