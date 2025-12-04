import numpy as np

with open("2025/day04/input.txt") as file_in:
    lines = []
    for line in file_in:
        temp_line = []
        for char in line.strip():
            temp_line.append(char)
        lines.append(temp_line)

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


total_removed = 0
removed = True

while removed:
    removed = False
    next_lines = lines.copy()

    for i in range(line_len):
        for j in range(line_len):
            if check_pos(i, j):
                next_lines[i][j] = "."
                removed = True
                total_removed += 1

    lines = next_lines.copy()

print(total_removed)
