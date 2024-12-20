import numpy as np

with open("input.txt") as file_in:
    l = []
    for line in file_in:
        l.append(list(line.strip()))

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

#l = []
#for line in example_string.splitlines():
#    l.append(list(line))

matrix = np.array(l)
#print(matrix)

# 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT
direction = 0
valid = True

def find_guard(m):
    i, j = np.where(m == "^")
    return i.item(), j.item()

def change_direction():
    global direction
    direction = (direction + 1) % 4

def in_bound(m, i, j):
    m_size = m.shape[0]
    return (0 <= i < m_size) and (0 <= j < m_size)

def count_X(m):
    return np.count_nonzero(m == "X")

def take_step(m, i, j):
    i_prev, j_prev = i, j
        
    if direction == 0: # step up
        i -= 1
    elif direction == 1: # step right
        j += 1
    elif direction == 2: # step down
        i += 1
    elif direction == 3:  # step left
        j -= 1

    if not in_bound(m, i, j):
        global valid
        valid = False
        m[i_prev, j_prev] = "X"
        return i, j

    # Check new coordinate
    if m[i, j] == "#":
        change_direction()
        return i_prev, j_prev
    elif m[i, j] == "." or m[i, j] == "X":
        m[i_prev, j_prev] = "X"
        m[i, j] = "^"
        return i, j

def main():
    i, j = find_guard(matrix)

    while valid:
        i, j = take_step(matrix, i, j)

    print(count_X(matrix))



main()
