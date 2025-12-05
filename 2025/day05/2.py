import re
import numpy as np

with open("2025/day05/input.txt") as file_in:
    ranges = []
    for line in file_in:
        if line.strip() == "":
            break
        temp = line.strip().split("-")
        ranges.append([int(temp[0]), int(temp[1])])

# Sort ranges
ranges.sort(key = lambda row: (row[0], row[1]))
range_l = [ranges[0]]

final_num = ranges[0][1]

for new_range in ranges[1:]:
    final_num = range_l[-1][1]

    if new_range[1] <= final_num:
        continue
    elif new_range[0] <= final_num:
        range_l.append([final_num + 1, new_range[1]])
    else:
        range_l.append(new_range)

    final_num = new_range[1]

res = 0
for r in range_l:
    res += r[1] + 1 - r[0]

print(res)
# 342433357244012
