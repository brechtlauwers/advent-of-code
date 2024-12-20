import numpy as np
from queue import Queue

with open("input.txt") as file_in:
    l = []
    for line in file_in:
        l.append(line.strip())

example_input = ["###############", "#.......#....E#", "#.#.###.#.###.#", "#.....#.#...#.#", "#.###.#####.#.#", "#.#.#.......#.#", "#.#.#####.###.#", "#...........#.#", "###.#.#####.#.#", "#...#.....#.#.#", "#.#.#.###.#.#.#", "#.....#...#.#.#", "#.###.#.#.#.#.#", "#S..#.....#...#", "###############"]

#m = np.array([list(x) for x in l])
m = np.array([list(x) for x in example_input])
m_len = m.shape[0]

start = (m_len-2, 1)
end = (1, m_len-2)

# UP = 0
# RIGHT = 1
# DOWN = 2
# LEFT = 3

def get_new_index(index, move_coord):
    return tuple(map(sum, zip(index, move_coord)))

def BFS(m, start, end):
    best_path = set()
    current_path = set()
    node_score = {start: 0}
    q = []
    q.append((start, "R"))

    while len(q) != 0:
        current_coord, direction = q.pop()
        print(current_coord)
        #print(node_score)
        current_score = node_score[current_coord]
        #print(current_score, direction)

        if current_coord == end and node_score.get(end, 1000000) > current_score + 1:
            node_score[end] = node_score[current_coord] + 1
            break
            
        up = get_new_index(current_coord, (-1, 0))
        right = get_new_index(current_coord, (0, 1))
        down = get_new_index(current_coord, (1, 0))
        left = get_new_index(current_coord, (0, -1))

        if direction == "U":
            update_score = (1, 1001, 1001, 1001)
            update_direction = "U"
        elif direction == "R":
            update_score = (1001, 1, 1001, 1001)
            update_direction = "R"
        elif direction == "D":
            update_score = (1001, 1001, 1, 1001)
            update_direction = "D"
        else:
            update_score = (1001, 1001, 1001, 1)
            update_direction = "L"

            
        if m[up] != "#" and node_score.get(up, 1000000) > current_score + update_score[0]:
            node_score[up] = current_score + update_score[0]
            q.append((up, "U"))
        if m[right] != "#" and node_score.get(right, 1000000) > current_score + update_score[1]:
            node_score[right] = current_score + update_score[1]
            q.append((right, "R"))
        if m[down] != "#" and node_score.get(down, 1000000) > current_score + update_score[2]:
            node_score[down] = current_score + update_score[2]
            q.append((down, "D"))
        if m[left] != "#" and node_score.get(left, 1000000) > current_score + update_score[3]:
            node_score[left] = current_score + update_score[3]
            q.append((left, "L"))
            
    return node_score[end]


print(BFS(m, start, end))
