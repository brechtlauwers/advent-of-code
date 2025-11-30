import re

with open("2023/day01/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip())

res = 0

for line in lines:
    d1 = re.search(r"\d", line)
    d2 = re.search(r"\d", line[::-1])
    res += int(d1.group(0) + d2.group(0))

print(res)
