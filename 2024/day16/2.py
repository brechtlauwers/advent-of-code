import numpy as np
from queue import Queue

with open("input.txt") as file_in:
    l = []
    for line in file_in:
        l.append(line.strip())

example_input = ["###############", "#.......#....E#", "#.#.###.#.###.#", "#.....#.#...#.#", "#.###.#####.#.#", "#.#.#.......#.#", "#.#.#####.###.#", "#...........#.#", "###.#.#####.#.#", "#...#.....#.#.#", "#.#.#.###.#.#.#", "#.....#...#.#.#", "#.###.#.#.#.#.#", "#S..#.....#...#", "###############"]

m = np.array([list(x) for x in l])
#m = np.array([list(x) for x in example_input])
m_len = m.shape[0]

start = (m_len-2, 1)
end = (1, m_len-2)


def visualise_path(m, path):
    #print(path)
    for i in range(m_len):
        for j in range(m_len):            
            if ((i, j)) in path:
                print("O", end="")
            else:
                print(m[i][j], end="")
        print()

def get_new_index(index, move_coord):
    return tuple(map(sum, zip(index, move_coord)))

def BFS(m, start, end):
    paths = []
    node_score = {start: 0}
    q = []
    q.append((start, "R", []))
    previous = {}

    while len(q) != 0:
        current_coord, direction, current_path = q.pop()
        #print(current_coord)
        #print(current_path)
        #visualise_path(m, current_path)
        current_score = node_score[current_coord]
        #print(current_score, direction)
        #print(current_coord)
        #print(node_score)

        if current_coord == end:
            paths.append((current_score, current_path))

        if current_coord == end and node_score.get(end, 1000000) > current_score + 1:
            node_score[end] = node_score[current_coord] + 1
            break
            
        up = get_new_index(current_coord, (-1, 0))
        right = get_new_index(current_coord, (0, 1))
        down = get_new_index(current_coord, (1, 0))
        left = get_new_index(current_coord, (0, -1))

        if direction == "U":
            update_score = (1, 1001, 1001, 1001)
        elif direction == "R":
            update_score = (1001, 1, 1001, 1001)
        elif direction == "D":
            update_score = (1001, 1001, 1, 1001)
        else:
            update_score = (1001, 1001, 1001, 1)
            
        if m[up] != "#":
            if node_score.get(up, 1000000) > current_score + update_score[0]:
                node_score[up] = current_score + update_score[0]
                new_path = current_path.copy()
                previous[current_coord] = previous.get(current_coord, 0)
                new_path.append(up)
                q.append((up, "U", new_path))

        if m[right] != "#":
            if node_score.get(right, 1000000) > current_score + update_score[1]:
                node_score[right] = current_score + update_score[1]
                new_path = current_path.copy()
                new_path.append(right)
                q.append((right, "R", new_path))

        if m[down] != "#":
            if node_score.get(down, 1000000) > current_score + update_score[2]:
                node_score[down] = current_score + update_score[2]
                new_path= current_path.copy()
                new_path.append(down)
                q.append((down, "D", new_path))
 
        if m[left] != "#":
            if node_score.get(left, 1000000) > current_score + update_score[3]:
                node_score[left] = current_score + update_score[3]
                new_path = current_path.copy()
                new_path.append(left)
                q.append((left, "L", new_path))

    final_set = set()
    for path in paths:
        if path[0] == node_score[end]:
            visualise_path(m, path[1])
            for x in path[1]:
                final_set.add(x)


    print(final_set)
    print(len(final_set))
    #print(node_score)

    
    # shortest_len = node_score[end]
    

    # paths = []
    # q = []
    # q.append((end, "L", []))
    # saves = []

    # while len(q) != 0:
    #     current_coord, direction, current_path = q.pop()
    #     #print(current_coord)
    #     #print(current_path)
    #     #visualise_path(m, current_path)
    #     current_score = node_score[current_coord]
    #     #print(current_score, direction)
    #     #print(current_coord)
    #     #print(node_score)

    #     if current_coord == start:
    #         paths.append((current_score, current_path))
    #     if current_coord == start and node_score.get(end, 1000000) > current_score + 1:
    #         break
            
    #     up = get_new_index(current_coord, (-1, 0))
    #     right = get_new_index(current_coord, (0, 1))
    #     down = get_new_index(current_coord, (1, 0))
    #     left = get_new_index(current_coord, (0, -1))

    #     if m[up] != "#":
    #         if node_score[up] < current_score:
    #             saves.append(up)
    #             q.append((up, "U", new_path))

    #     if m[right] != "#":
    #         if node_score[right] < current_score:
    #             saves.append(right)
    #             q.append((right, "R", new_path))

    #     if m[down] != "#":
    #         if node_score[down] < current_score:
    #             saves.append(down)
    #             q.append((down, "D", new_path))

    #     if m[left] != "#":
    #         if node_score[left] < current_score:
    #             saves.append(left)
    #             q.append((left, "L", new_path))
    # print(saves)
    # visualise_path(m, saves)

    return node_score[end]


print(BFS(m, start, end))

532 - 545
