import numpy as np

with open("input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip())

res = 0

for bank in lines:
    list_batt = [int(x) for x in list(bank)]
    ptr1 = np.argmax(list_batt[:-1])
    max1 = list_batt[ptr1]

    new_list = list_batt[ptr1 + 1:]
    
    ptr2 = np.argmax(new_list)
    max2 = new_list[ptr2]

    res += int(str(max1) + str(max2))

print(res)
