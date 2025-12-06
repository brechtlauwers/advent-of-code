import numpy as np
import math


with open("2025/day06/input.txt") as file_in:
    lines = []
    for line in file_in:
        line = line.strip('\n')
        lines.append(list(line))

line_m = np.array(lines).T
current_numlist = []
res = 0

for line in line_m:
    if current_numlist == []:
        operator = line[-1]

    num = ''.join(line[:-1])
    if num.isspace():
        if operator == "+":
            res += sum(current_numlist)
        elif operator == "*":
            res += math.prod(current_numlist)
        current_numlist = []
    else:
        num = int(num)
        current_numlist.append(num)

if operator == "+":
    res += sum(current_numlist)
elif operator == "*":
    res += math.prod(current_numlist)
print(res)
