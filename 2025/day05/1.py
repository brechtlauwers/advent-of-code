import re
import numpy as np

with open("2025/day05/input.txt") as file_in:
    ranges, ids = [], []
    range_bool = True
    for line in file_in:
        if line.strip() == "":
            range_bool = False
            continue

        if range_bool:
            ranges.append(line.strip())
        else:
            ids.append(int(line.strip()))
res = 0

for idx in ids:
    for r in ranges:
        num = r.split("-")

        if int(num[0]) <= idx and idx <= int(num[1]):
            res += 1
            break

print(res)
