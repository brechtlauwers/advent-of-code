import numpy as np

with open("input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip())

res = 0

for bank in lines:
    list_batt = [int(x) for x in list(bank)]
    max_vals = []
    
    for i in range(12, 0, -1):
        if i == 1:
            sublist = list_batt
        else:
            sublist = list_batt[:(-i + 1)]

        ptr = np.argmax(sublist)
        val = sublist[ptr]

        list_batt = list_batt[ptr+1:]
        max_vals.append(val)

    res += int(''.join([str(x) for x in max_vals]))

print(res)
