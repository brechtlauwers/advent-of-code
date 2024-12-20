import numpy as np
from queue import Queue


with open("input.txt") as file_in:
    l = []
    for line in file_in:
        l.append(list(line.strip()))

example_string = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

# l = []
# for line in example_string.splitlines():
#    l.append(list(line))

m = np.array(l)
m_len = m.shape[0]
res = 0


def check_region(i, j):
    Q = Queue()
    region_res, perimeter = 0, 0
    region_index = []
    plant = m[i][j]
    Q.put((i,j))
    
    while not Q.empty():
        index = Q.get()
        if m[index] == plant:
            m[index] = "#"
            region_index.append(index)
            region_res += 1
            
            if 0 <= index[0] + 1 < m_len:
                Q.put((index[0] + 1, index[1]))
                if (index[0] + 1, index[1]) not in region_index and m[index[0] + 1, index[1]] != plant:
                    perimeter += 1
            else:
                perimeter += 1
            
                
            if 0 <= index[0] - 1 < m_len:
                Q.put((index[0] - 1, index[1]))
                if (index[0] - 1, index[1]) not in region_index and m[index[0] - 1, index[1]] != plant:
                    perimeter += 1
            else:
                perimeter += 1
                
            if 0 <= index[1] + 1 < m_len:
                Q.put((index[0], index[1] + 1))
                if (index[0], index[1] + 1) not in region_index and m[index[0], index[1] + 1] != plant:
                    perimeter += 1
            else:
                perimeter += 1

            if 0 <= index[1] - 1 < m_len:
                Q.put((index[0], index[1] - 1))
                if (index[0], index[1] - 1) not in region_index and m[index[0], index[1] - 1] != plant:
                    perimeter += 1
            else:
                perimeter += 1

    # print("Perimeter: ")
    # print(perimeter)
    # print(region_res)
    return (region_res * perimeter)

for i in range(m_len):
    for j in range(m_len):
        plant = m[i][j]
        if plant != "#":
            res += check_region(i, j)

print(res)

