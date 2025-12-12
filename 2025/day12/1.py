
with open("2025/day12/input.txt") as file_in:
    shapes = dict()
    cur_shape = []
    next_part = False

    for line in file_in:
        line = line.strip()
        if "x" in line and not next_part:
            next_part = True
            grids = [[int(line[:2]),
                      int(line[3:5]),
                      [int(x) for x in line[7:].split()]]]
            continue

        if next_part:
            grids.append([int(line[:2]),
                          int(line[3:5]),
                          [int(x) for x in line[7:].split()]])
        else:
            if len(line.strip()) == 0:
                shapes[cur_shape[0][0]] = [x for x in cur_shape[1:]]
                cur_shape = []
            else:
                cur_shape.append(line.strip())


max_size = 8
count = 0

for line in grids:
    x, y, shape_amount = line
    count += sum(shape_amount) * max_size <= x * y

print(count)

