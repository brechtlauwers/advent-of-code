import numpy as np

with open("2025/day09/input.txt") as file_in:
    lines = []
    for line in file_in:
        x, y = line.strip().split(',')
        lines.append((int(x), int(y)))


def surface(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return abs((y2 - y1 + 1) * (x2 - x1 + 1))


max_surf = 0

for coord_i in lines:
    for coord_j in lines:
        new_surf = surface(coord_i, coord_j)
        if new_surf > max_surf:
            max_surf = new_surf

print(max_surf)
