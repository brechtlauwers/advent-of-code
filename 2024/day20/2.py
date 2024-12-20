import numpy as np
from queue import Queue

with open("input.txt") as file_in:
    l = []
    for line in file_in:
        l.append(line.strip())

#example_input = ["###############", "#...#...#.....#", "#.#.#.#.#.###.#", "#S#...#.#.#...#", "#######.#.#.###", "#######.#.#...#", "#######.#.###.#", "###..E#...#...#", "###.#######.###", "#...###...#...#", "#.#####.#.###.#", "#.#...#.#.#...#", "#.#.#.#.#.#.###", "#...#...#...###", "###############"]

m = np.array([list(x) for x in l])
#m = np.array([list(x) for x in example_input])
m_len = m.shape[0]


def find_start_end(m):
    S = np.where(m == 'S')
    E = np.where(m == 'E')    
    return (int(S[0][0]), int(S[1][0])), (int(E[0][0]), int(E[1][0]))


def get_new_index(index, move_coord):
    return tuple(map(sum, zip(index, move_coord)))

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        last = path[-1]
        path.append(parent[last])
    path.reverse()
    return path

def get_adjacent(m, v):
    m_len = m.shape[0]
    
    up = get_new_index(v, (-1, 0))
    right = get_new_index(v, (0, 1))
    down = get_new_index(v, (1, 0))
    left = get_new_index(v, (0, -1))

    adj_l = []

    if 0 <= up[0] < m_len and 0 <= up[1] < m_len:
        if m[up] == "." or m[up] == "E":
            adj_l.append(up)

    if 0 <= right[0] < m_len and 0 <= right[1] < m_len:
        if m[right] == "." or m[right] == "E":
            adj_l.append(right)
            
    if 0 <= down[0] < m_len and 0 <= down[1] < m_len:
        if m[down] == "." or m[down] == "E":
            adj_l.append(down)
            
    if 0 <= left[0] < m_len and 0 <= left[1] < m_len:
        if m[left] == "." or m[left] == "E":
            adj_l.append(left)
            
    return adj_l
    

def BFS(m, start, end):
    parent = {}
    q = Queue()
    explored = set(start)
    q.put(start)

    while not q.empty():
        v = q.get()
        if v == end:
            return backtrace(parent, start, end)

        all_adjacent = get_adjacent(m, v)
        for adj in all_adjacent:
            if adj not in explored:
                explored.add(adj)
                parent[adj] = v
                q.put(adj)


def check_shortcut(m, current_i, path, done):
    m_len = m.shape[0]
    current = path[current_i]
    cur_x, cur_y = current[0], current[1]
    
    # list of possible shortcut coordinates
    possible = set()
    
    for path_pos in path[current_i:]:
        pos_x, pos_y = path_pos[0], path_pos[1]
        distance = abs(cur_x - pos_x) + abs(cur_y - pos_y)
        if distance <= 20:
            possible.add((distance, path_pos))
    return possible


def path_saved(res, path, count_dict, pos_i, path_len):
    if res is not None:
        for possible in res:
            distance = possible[0]
            shortcut = possible[1]
            shortcut_i = path.index(shortcut)
            if shortcut_i > pos_i:
                new_len = path_len - (shortcut_i - pos_i) + distance
                saves = path_len - new_len
                if saves >= 100:
                    count_dict[saves] = count_dict.get(saves, 0) + 1


def shortcut(m, path):
    count_dict = {}
    done = set()
    
    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)
    
    path_len = len(path)
    
    for pos_i in range(path_len):
        current = path[pos_i]
        res = check_shortcut(m, pos_i, path, done)
        path_saved(res, path, count_dict, pos_i, path_len)

    counter = 0
    for key, value in sorted(count_dict.items()):
        if key >= 100:
            counter += value

    return counter


start, end = find_start_end(m)
path = BFS(m, start, end)

print(shortcut(m, path))
