import numpy as np


with open("2025/day02/input.txt") as file_in:
    lines = []
    for full_line in file_in:
        lines = full_line.split(',')

res = 0

for ids in lines:
    id_start, id_stop = ids.split('-')

    for idx in range(int(id_start), int(id_stop) + 1):
        temp_res = []

        id_len = len(str(idx))

        for digits in range(1, (id_len // 2) + 1):
            first_piece = str(idx)[:digits]
            if str(idx) == (first_piece * (id_len // len(first_piece))):
                temp_res.append(str(idx))

        res += sum(int(x) for x in list(set(temp_res)))

print(res)
