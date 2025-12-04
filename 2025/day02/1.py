import numpy as np


with open("2025/day02/input.txt") as file_in:
    lines = []
    for full_line in file_in:
        lines = full_line.split(',')

res = 0

for ids in lines:
    id_start, id_stop = ids.split('-')

    for idx in range(int(id_start), int(id_stop) + 1):
        id_len = len(str(idx))

        if id_len % 2 == 1:  # uneven
            continue

        first_half = str(idx)[:id_len // 2]
        last_half = str(idx)[id_len // 2:]

        if first_half == last_half:
            res += idx

print(res)
