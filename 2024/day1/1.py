import numpy as np

with open("input.txt") as file_in:
    l1, l2 = [], []
    for line in file_in:
        n1, n2 = line.split()
        l1.append(int(n1))
        l2.append(int(n2))

l1 = np.array(sorted(l1))
l2 = np.array(sorted(l2))

print(np.sum(np.absolute(l1 - l2)))
