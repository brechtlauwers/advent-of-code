import numpy as np
import re
from queue import Queue 

with open("input.txt") as file_in:
    l = []
    for line in file_in:
        x, y = re.findall(r"\d+,\d+", line.strip())[0].split(',')
        l.append((int(x), int(y)))

# l = []
# ex_l=["5,4","4,2","4,5","3,0","2,1","6,3","2,4","1,5","0,6","3,3","2,6","5,1","1,2","5,5","2,5","6,5","1,4","0,4","6,4","1,1","6,1","1,0","0,5","1,6","2,0"]
# for el in ex_l:
#     x, y = el.split(',')
#     l.append((int(x), int(y)))
# m = np.full((7,7), ".")

m = np.full((71,71), ".")
start = (0,0)
#end = (6,6)
end = (70,70)

def visualise_path(m, path):
    m_len = m.shape[0]
    for i in range(m_len):
        for j in range(m_len):            
            if ((i, j)) in path:
                print("O", end="")
            else:
                print(m[i][j], end="")
        print()

def drop_bits(m, l, bits):
    for i in range(bits):
        y, x = l[i]
        m[x][y] = "#"
    return m

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        last = path[-1]
        path.append(parent[last])
    path.reverse()
    return path

def get_new_index(index, move_coord):
    return tuple(map(sum, zip(index, move_coord)))

def get_adjacent(m, v):
    m_len = m.shape[0]
    
    up = get_new_index(v, (-1, 0))
    right = get_new_index(v, (0, 1))
    down = get_new_index(v, (1, 0))
    left = get_new_index(v, (0, -1))

    adj_l = []

    if 0 <= up[0] < m_len and 0 <= up[1] < m_len:
        if m[up] == ".":
            adj_l.append(up)

    if 0 <= right[0] < m_len and 0 <= right[1] < m_len:
        if m[right] == ".":
            adj_l.append(right)
            
    if 0 <= down[0] < m_len and 0 <= down[1] < m_len:
        if m[down] == ".":
            adj_l.append(down)
            
    if 0 <= left[0] < m_len and 0 <= left[1] < m_len:
        if m[left] == ".":
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
                   

path = []
bits = 1024
#bits = 2950
while path is not None and bits <= len(l):
    #print(f"bits: {bits}; coord: {l[bits-1]}")
    m = drop_bits(m, l, bits)
    path = BFS(m, start, end)
    bits += 1
    if path is None:
        print(l[bits-2])

