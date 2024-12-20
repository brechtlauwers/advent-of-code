import numpy as np

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

m = np.array([list(x) for x in map_l])

# Example input
# m = np.array([list (x) for x in ["##########", "#..O..O.O#", "#......O.#", "#.OO..O.O#", "#..O@..O.#", "#O#..O...#", "#O..O..O.#", "#.OO.O.OO#", "#....O...#", "##########"]])
# moves = "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"

def count_result(m):
    res = 0
    for i in range(1, m.shape[0] - 1):
        for j in range(1, m.shape[0] - 1):
            if m[i][j] == "O":
                res += 100 * i + j
    return res

def find_robot(m):
    x, y = np.where(m=="@")
    return x[0], y[0]

def get_new_index(robot_index, move_coord):
    return tuple(map(sum, zip(robot_index, move_coord)))

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
    else:                       # This part tries to move the "O"
        while m[new_index] == "O":
            new_index = get_new_index(new_index, move_coord)
        if m[new_index] == ".":
            m[new_index] = "O"
            m[robot_index] = "."
            new_index = get_new_index(robot_index, move_coord)
            m[new_index] = "@"
        elif m[new_index] == "#":
            new_index = robot_index

    return m, new_index



robot_index = find_robot(m)

for move in moves:
    m, robot_index = make_move(m, robot_index, move)
    #print(move, robot_index)
    #print(m)

print(m)
print(count_result(m))
    
