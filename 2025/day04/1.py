import numpy as np

with open("2025/day04/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip())

line_len = len(lines[0])


def check_pos(pos_i, pos_j):
    if lines[pos_i][pos_j] == ".":
        return

    res = 0

    for i in range(pos_i - 1, pos_i + 2):
        for j in range(pos_j - 1, pos_j + 2):
            if i == pos_i and j == pos_j:
                continue
            if i < 0 or i >= line_len:
                continue
            if j < 0 or j >= line_len:
                continue

            if lines[i][j] == "@":
                res += 1

    if res < 4:
        return True
    else:
        return False


final_res = 0
for i in range(line_len):
    for j in range(line_len):
        if check_pos(i, j):
            final_res += 1

print(final_res)
