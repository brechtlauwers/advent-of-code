import numpy as np
from queue import Queue

with open("input.txt") as file_in:
    moves = ""
    map_l = []
    movements = False
    for line in file_in:
        if line == '\n':
            movements = True
            continue
        if movements:
            moves += line.strip()
        else:
            map_l.append(line.strip())


# ##Example input
# map_l = ["##########", "#..O..O.O#", "#......O.#", "#.OO..O.O#", "#..O@..O.#", "#O#..O...#", "#O..O..O.#", "#.OO.O.OO#", "#....O...#", "##########"]
# m = np.array([list (x) for x in map_l])
# moves = "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"

new_map_l = []
for line in map_l:
    new_line = []
    for obj in line:
        if obj == "#":
            new_line += (["#", "#"])
        elif obj == "O":
            new_line += (["[", "]"])
        elif obj == ".":
            new_line += ([".", "."])
        elif obj == "@":
            new_line += (["@", "."])
    new_map_l.append(new_line)

m = np.array(new_map_l)


def count_result(m):
    res = 0
    
    for i in range(1, m.shape[0] - 1):
        for j in range(1, m.shape[1] - 1):
            if m[i][j] == "[":
                
                res += 100 * i + j
    return res

def find_robot(m):
    x, y = np.where(m=="@")
    return x[0], y[0]

def get_new_index(robot_index, move_coord):
    return tuple(map(sum, zip(robot_index, move_coord)))

## Move box left
def move_box_left(m, robot_index, new_index):
    L, R = (0, -1), (0, 1)
    new_robot_index = get_new_index(robot_index, L)
    
    while m[new_index] == "[" or m[new_index] == "]":
        new_index = get_new_index(new_index, L)
    if m[new_index] == ".":
        while new_index != new_robot_index:
            m[new_index] = "["
            new_index = get_new_index(new_index, R)
            m[new_index] = "]"
            new_index = get_new_index(new_index, R)
        m[robot_index] = "."
        m[new_robot_index] = "@"
    elif m[new_index] == "#":
        new_robot_index = robot_index

    return m, new_robot_index


## Move box right
def move_box_right(m, robot_index, new_index):
    L, R = (0, -1), (0, 1)
    new_robot_index = get_new_index(robot_index, R)
    
    while m[new_index] == "[" or m[new_index] == "]":
        new_index = get_new_index(new_index, R)
    if m[new_index] == ".":
        while new_index != new_robot_index:
            m[new_index] = "]"
            new_index = get_new_index(new_index, L)
            m[new_index] = "["
            new_index = get_new_index(new_index, L)
        m[robot_index] = "."
        m[new_robot_index] = "@"
    elif m[new_index] == "#":
        new_robot_index = robot_index

    return m, new_robot_index


## Move box up
def move_box_up(m, robot_index, new_index):
    L, R = (0, -1), (0, 1)
    U, D = (-1, 0), (1, 0)
    new_robot_index = new_index
    to_move = []                # This represents a stack!
    box_queue = Queue()
    no_wall = True
    
    if m[new_index] == "[":
        to_move.append(new_index)
        box_queue.put(new_index)
    if m[new_index] == "]":
        left_box_index = get_new_index(new_index, L)
        to_move.append(left_box_index)
        box_queue.put(left_box_index)

    while not box_queue.empty():
        box_index = box_queue.get()
        new_left_index = get_new_index(box_index, U)
        new_right_index = get_new_index(new_left_index, R)

        if m[new_left_index] == "#" or m[new_right_index] == "#":
            no_wall = False
            break
        
        if m[new_left_index] == "[":
            to_move.append(new_left_index)
            box_queue.put(new_left_index)
        if m[new_left_index] == "]":
            new_box_index = get_new_index(new_left_index, L)
            to_move.append(new_box_index)
            box_queue.put(new_box_index)
        if m[new_right_index] == "[":
            to_move.append(new_right_index)
            box_queue.put(new_right_index)

    if no_wall:
        while len(to_move) != 0:
            box_index = to_move.pop()
            right_box_index = get_new_index(box_index, R)
            m[box_index] = "."
            m[right_box_index] = "."
            new_left_index = get_new_index(box_index, U)
            new_right_index = get_new_index(new_left_index, R)
            m[new_left_index] = "["
            m[new_right_index] = "]"
            
        m[robot_index] = "."
        m[new_robot_index] = "@"
    else:
        new_robot_index = robot_index
    return m, new_robot_index


## Move box down
def move_box_down(m, robot_index, new_index):
    L, R = (0, -1), (0, 1)
    U, D = (-1, 0), (1, 0)
    new_robot_index = new_index
    to_move = []                # This represents a stack!
    box_queue = Queue()
    no_wall = True
    
    if m[new_index] == "[":
        to_move.append(new_index)
        box_queue.put(new_index)
    if m[new_index] == "]":
        left_box_index = get_new_index(new_index, L)
        to_move.append(left_box_index)
        box_queue.put(left_box_index)

    while not box_queue.empty():
        box_index = box_queue.get()
        new_left_index = get_new_index(box_index, D)
        new_right_index = get_new_index(new_left_index, R)

        if m[new_left_index] == "#" or m[new_right_index] == "#":
            no_wall = False
            break
        
        if m[new_left_index] == "[":
            to_move.append(new_left_index)
            box_queue.put(new_left_index)
        if m[new_left_index] == "]":
            new_box_index = get_new_index(new_left_index, L)
            to_move.append(new_box_index)
            box_queue.put(new_box_index)
        if m[new_right_index] == "[":
            to_move.append(new_right_index)
            box_queue.put(new_right_index)

    if no_wall:
        while len(to_move) != 0:
            box_index = to_move.pop()
            right_box_index = get_new_index(box_index, R)
            m[box_index] = "."
            m[right_box_index] = "."
            new_left_index = get_new_index(box_index, D)
            new_right_index = get_new_index(new_left_index, R)
            m[new_left_index] = "["
            m[new_right_index] = "]"
            
        m[robot_index] = "."
        m[new_robot_index] = "@"
    else:
        new_robot_index = robot_index
    return m, new_robot_index



def make_move(m, robot_index, move):
    if move == "<":
        move_coord = (0, -1)
    elif move == "^":
        move_coord = (-1, 0)
    elif move == ">":
        move_coord = (0, 1)
    else:
        move_coord = (1, 0)

    new_index = get_new_index(robot_index, move_coord)
            
    if m[new_index] == ".":
        m[robot_index] = "."
        m[new_index] = "@"
    elif m[new_index] == "#":
        new_index = robot_index
    else:                       # This part tries to move the "[]" CHANGE THIS FOR PART 2
        if move == "<":
            m, new_index = move_box_left(m, robot_index, new_index)
        elif move == ">":
            m, new_index = move_box_right(m, robot_index, new_index)
        elif move == "^":
            m, new_index = move_box_up(m, robot_index, new_index)
        else:
            m, new_index = move_box_down(m, robot_index, new_index)

    return m, new_index


def make_move(m, robot_index, move):
    if move == "<":
        move_coord = (0, -1)
    elif move == "^":
        move_coord = (-1, 0)
    elif move == ">":
        move_coord = (0, 1)
    else:
        move_coord = (1, 0)

    new_index = get_new_index(robot_index, move_coord)
            
    if m[new_index] == ".":
        m[robot_index] = "."
        m[new_index] = "@"
    elif m[new_index] == "#":
        new_index = robot_index
    else:                       # This part tries to move the "[]" CHANGE THIS FOR PART 2
        if move == "<":
            m, new_index = move_box_left(m, robot_index, new_index)
        elif move == ">":
            m, new_index = move_box_right(m, robot_index, new_index)
        elif move == "^":
            m, new_index = move_box_up(m, robot_index, new_index)
        else:
            m, new_index = move_box_down(m, robot_index, new_index)

    return m, new_index


robot_index = find_robot(m)

for move in moves:
    m, robot_index = make_move(m, robot_index, move)
    #print(move, robot_index)
    #print(m)

for x in m:
    print(*x)
print(count_result(m))
    
