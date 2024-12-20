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


def check_shortcut(m, current, direction, L, R, done):
    m_len = m.shape[0]
    s_1 = get_new_index(current, direction)
    s_2 = get_new_index(s_1, direction)

    # positions next to the number 2 in the shortcut
    s_U = get_new_index(s_2, direction)
    s_L = get_new_index(s_2, L)
    s_R = get_new_index(s_2, R)

    # list of possible shortcut coordinates
    possible = []

    # no shortcut can go to the map edge
    if not (0 < s_2[0] < m_len - 1 and 0 < s_2[1] < m_len - 1):
        return None

    # do not follow the normal path
    if m[s_1] != "#":
        return None

    done.add(s_R)
    done.add(s_L)
    done.add(s_U)

    # s_2 is on the path
    if (m[s_2] == "." or m[s_2] == "E"):
        return [(0, s_2)]

    # cases of places next to s_2
    # (1, X) because you need to take an extra step to the side
    if (m[s_U] == "." or m[s_U] == "E") and s_U not in done:
        possible.append((1, s_U))
    if (m[s_L] == "." or m[s_L] == "E") and s_L not in done:
        possible.append((1, s_L))
    if (m[s_R] == "." or m[s_R] == "E") and s_R not in done:
        possible.append((1, s_R))

    return possible


def path_saved(res, path, count_dict, pos_i, path_len):
    if res is not None:
        for possible in res:
            extra_step = possible[0]
            shortcut = possible[1]
            shortcut_i = path.index(shortcut)
            if shortcut_i > pos_i:
                new_len = path_len - (shortcut_i - pos_i) + extra_step + 2
                saves = path_len - new_len
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
        res_up = check_shortcut(m, current, up, left, right, done)
        res_right = check_shortcut(m, current, right, up, down, done)
        res_down = check_shortcut(m, current, down, right, left, done)
        res_left = check_shortcut(m, current, left, down, up, done)

        path_saved(res_up, path, count_dict, pos_i, path_len)
        path_saved(res_right, path, count_dict, pos_i, path_len)
        path_saved(res_left, path, count_dict, pos_i, path_len)
        path_saved(res_down, path, count_dict, pos_i, path_len)

    counter = 0
    for key, value in sorted(count_dict.items()):
        if key >= 100:
            counter += value
    return counter


start, end = find_start_end(m)
path = BFS(m, start, end)

print(shortcut(m, path))
