import numpy as np

def find_guard(m):
    i, j = np.where(m == "^")
    return i.item(), j.item()

def change_direction(current):
    return (current + 1) % 4

def in_bound(m, i, j):
    rows, cols = m.shape
    return 0 <= i < rows and 0 <= j < cols

def go_forward(i, j, direction):
    if direction == 0:  # up
        i -= 1
    elif direction == 1:  # right
        j += 1
    elif direction == 2:  # down
        i += 1
    elif direction == 3:  # left
        j -= 1
    return i, j

def take_step(m, i, j, direction):
    i_prev, j_prev = i, j
    i, j = go_forward(i, j, direction)

    if not in_bound(m, i, j):
        return i_prev, j_prev, change_direction(direction), False

    if m[i, j] == "#":
        return i_prev, j_prev, change_direction(direction), True
    elif m[i, j] == ".":
        m[i_prev, j_prev] = "X"
        m[i, j] = "^"
        return i, j, direction, True

    return i_prev, j_prev, direction, True

def try_place_object(m, i, j, direction, result_counter):
    if not in_bound(m, i, j) or m[i, j] == "#":
        return result_counter

    m[i, j] = "O"
    in_bound_flag = True
    svs = []
    initial_i, initial_j = find_guard(m)

    i, j = initial_i, initial_j
    while in_bound_flag:
        i, j, direction, in_bound_flag = take_step(m, i, j, direction)
        state = (i, j, direction)
        if state in svs:
            result_counter += 1
            break
        svs.append(state)

    return result_counter

def main():
    example_string = """....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#..."""

    l = [list(line) for line in example_string.splitlines()]
    matrix = np.array(l)

    i, j = find_guard(matrix)
    direction = 0
    valid = True
    result_counter = 0

    while valid:
        matrix_copy = np.copy(matrix)
        result_counter = try_place_object(matrix_copy, i, j, direction, result_counter)
        i, j, direction, valid = take_step(matrix, i, j, direction)

    print(result_counter)

main()
