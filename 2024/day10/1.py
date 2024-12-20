import numpy as np

with open("input.txt") as file_in:
    l = []
    for line in file_in:
        l.append(list(line.strip()))

example_string = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


#l = []
#for line in example_string.splitlines():
#    l.append(list(line))

m = np.array(l)
m_len = m.shape[0]
res = set()

def find_trail(curr_index, m):
    i, j = curr_index[0], curr_index[1]
    if m[i][j] == "9":
        global res
        res.add((i,j))
    
    next_val = int(m[i][j])
    up = (i - 1, j)
    down = (i + 1, j)
    left = (i, j + 1)
    right = (i, j - 1)

    if 0 <= up[0] < m.shape[0] and 0 <= up[1] < m.shape[1]:
        if int(m[up]) == next_val + 1:
            find_trail(up, m)
    if 0 <= down[0] < m.shape[0] and 0 <= down[1] < m.shape[1]:
        if int(m[down]) == next_val + 1:
            find_trail(down, m)
    if 0 <= left[0] < m.shape[0] and 0 <= left[1] < m.shape[1]:
        if int(m[left]) == next_val + 1:
            find_trail(left, m)
    if 0 <= right[0] < m.shape[0] and 0 <= right[1] < m.shape[1]:
        if int(m[right]) == next_val + 1:
            find_trail(right, m)
    
total = 0
for i in range(m_len):
    for j in range(m_len):
        if m[i][j] == "0":
            find_trail((i, j), m)
            total += len(res)
            res.clear()
print(total)
