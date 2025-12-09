import numpy as np
import functools

with open("2025/day09/input.txt") as file_in:
    lines = []
    for line in file_in:
        x, y = line.strip().split(',')
        lines.append((int(x), int(y)))


max_side = 100_000


def surface(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return abs((y2 - y1 + 1) * (x2 - x1 + 1))


def get_line(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    if x1 == x2:
        line = [(x1, y) for y in range(y1 + 1, y2)]
    else:
        line = [(x, y1) for x in range(x1 + 1, x2)]

    line.append(c1)
    line.append(c2)
    return line


@functools.cache
def in_shape(coord, line_set):
    if coord in line_set:
        return True
    x, y = coord
    count = 0
    for move_x in range(x + 1, max_side):
        if (move_x, y) in line_set:
            count += 1
    if count % 2 == 1:
        return True
    else:
        return False


# MAIN
print("Getting lines")
line_set = set()

# Get coordinates from all the lines
for i in range(1, len(lines)):
    coord_i = lines[i-1]
    coord_j = lines[i]
    line_set.update(set(get_line(coord_i, coord_j)))
line_set.update(set(get_line(lines[0], lines[-1])))

print("Calculate surfaces")

# Calculate all possible surfaces between coordinates and sort
all_surf = []
for coord_i in lines:
    for coord_j in lines:
        if coord_i == coord_j:
            continue
        all_surf.append((surface(coord_i, coord_j), (coord_i, coord_j)))
all_surf.sort(key=lambda s: s[0], reverse=True)

print("Loop all surfaces")
line_set = frozenset(line_set)

for tup in all_surf:
    surf, coord = tup
    if surf > 1_396_494_460:
        continue

    print(tup)
    x1, y1 = coord[0]
    x3, y3 = coord[1]

    if x1 > x3:
        x1, x3 = x3, x1
    if y1 > y3:
        y1, y3 = y3, y1

    x2, y2 = x1, y3
    x4, y4 = x3, y1

    surf_line_set = set()
    surf_line_set.update(get_line((x1, y1), (x2, y2)))
    surf_line_set.update(get_line((x2, y2), (x3, y3)))
    surf_line_set.update(get_line((x3, y3), (x4, y4)))
    surf_line_set.update(get_line((x4, y4), (x1, y1)))

    valid = True

    for curr_coord in surf_line_set:
        if not in_shape(curr_coord, line_set):
            valid = False
            break

    if valid:
        print(f"final tuple: {tup}")
        break


# Too high: 3_590_867_268
# Not:      1_396_463_530
