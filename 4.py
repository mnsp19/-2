import csv
import random

with open('scientist.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    symparol = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for r in reader:
        Name = r['ScientistName'].split()
        r['login'] = f'{Name[0]}_{Name[1][0]}{Name[2][0]}'
        parol = ''
        for i in range(10):
            parol += random.choice(symparol)
        r['parol'] = parol

    with open('scientist_password.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, delimiter='#', fieldnames =['ScientistName', 'preparation', 'date', 'components', 'login', 'parol'])
        writer.writeheader()
        writer.writerows(reader)