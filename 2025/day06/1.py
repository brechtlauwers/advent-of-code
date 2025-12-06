import numpy as np
import math


with open("2025/day06/input.txt") as file_in:
    lines = []
    for line in file_in:
        line = line.strip().split()
        lines.append(line)

lines = np.array(lines)
len_lines = lines.shape[0]
res = 0

for i, operation in enumerate(lines[-1]):
    all_num = [int(lines[j][i]) for j in range(len_lines - 1)]

    if operation == "+":
        res += sum(all_num)
    elif operation == "*":
        res += math.prod(all_num)

print(res)
