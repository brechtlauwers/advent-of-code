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

valid = True
result_counter = set()


def find_guard(m):
    i, j = np.where(m == "^")
    return i.item(), j.item()

initial_i, initial_j = find_guard(matrix)


# 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT
def change_direction(current):
    return (current + 1) % 4

def in_bound(m, i, j):
    m_size = m.shape[0]
    return (0 <= i < m_size) and (0 <= j < m_size)

def go_forward(m, i, j, direction):
    if direction == 0: # step up
        i -= 1
    elif direction == 1: # step right
        j += 1
    elif direction == 2: # step down
        i += 1
    elif direction == 3:  # step left
        j -= 1
    return i, j


def take_step(m, i, j, direction):
    i_prev, j_prev = i, j
    i, j = go_forward(m, i, j, direction)

    if not in_bound(m, i, j):
        global valid
        valid = False
        m[i_prev, j_prev] = "X"
        return i, j, direction

    # Check new coordinate
    if m[i, j] == "#":
        new_direction = change_direction(direction)
        return i_prev, j_prev, new_direction
    elif m[i, j] == "." or m[i, j] == "X":
        m[i_prev, j_prev] = "X"
        m[i, j] = "^"
        return i, j, direction


def take_object_step(m, i, j, direction, svs):
    global result_counter
    i_prev, j_prev = i, j
    i, j = go_forward(m, i, j, direction)

    if not in_bound(m, i, j):
        m[i_prev, j_prev] = "X"
        return (i, j, direction, False, svs)

    # Check new coordinate
    if m[i, j] == "#" or m[i, j] == "O":
        new_direction = change_direction(direction)
        if (i, j, new_direction) in svs:
            #print("HERE")
            #print(m)
            return (i, j, direction, "O", svs)
        svs.append(tuple((i,j,new_direction)))
        return (i_prev, j_prev, new_direction, True, svs)
    #elif m[i, j] == "O":
    #    return (i, j, direction, "O", svs)
    elif m[i, j] == "." or m[i, j] == "X" or m[i, j] == "^":
        m[i_prev, j_prev] = "X"
        m[i, j] = "^"
        return (i, j, direction, True, svs)


def try_place_object(m, i, j, direction):
    global result_counter, initial_i, initial_j
    i_object, j_object = go_forward(m, i, j, direction)
    i_new, j_new = i, j

    if not in_bound(m, i_object, j_object):
        return
    
    if m[i_object, j_object] == "#":
        return
    
    m[i_object, j_object] = "O"
    

    in_bnd = True
    svs = []
    
    direction = 0
    i, j = initial_i, initial_j
    
 
    while in_bnd:
        i, j, direction, in_bnd, svs = take_object_step(m, i, j, direction, svs)
        if in_bnd == "O":
            result_counter.add(tuple((i_object, j_object)))
            #print(m)
            
            in_bnd = False
    #m[i_new, j_new] = "."


def main():
    i, j = find_guard(matrix)
    direction = 0

    while valid:
        #print(matrix)
        try_place_object(np.copy(matrix), i, j, direction)
        
        i, j, direction = take_step(matrix, i, j, direction)
        #print(matrix)

    print(len(result_counter))


main()

# 1673 too high
# 1546 too high

# New idea, place an obstruction at a valid location and check for loops.
