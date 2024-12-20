import numpy as np
from collections import Counter

with open("input.txt") as file_in:
    l1, l2 = [], []
    for line in file_in:
        n1, n2 = line.split()
        l1.append(int(n1))
        l2.append(int(n2))

l1 = np.array(l1)
l2 = np.array(l2)

score = 0
ctr = Counter(l2)

for number in l1:
    score += ctr[number] * number

print(score)
