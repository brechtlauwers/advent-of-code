import re
import os

print(os.getcwd())

with open("./input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.rstrip('\n'))

res = 0
        
for line in lines:
    d1 = re.search(r"\d", line)
    d2 = re.search(r"\d", line[::-1])
    res += int(d1.group(0) + d2.group(0))

print(res)
