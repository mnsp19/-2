import csv
import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    er = [n for n in nums if n['date'] < q['date']]
    fs = [q] * nums.count(q)
    k = [n for n in nums if n['date'] > q['date']]
    return quicksort(er) + fs + quicksort(k)


with open('scientist (1).txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    reader = quicksort(reader)

with open('scientist (1).txt', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['ScientistName', 'preparation', 'date', 'components'], delimiter='#')
    writer.writeheader()
    writer.writerows(reader)