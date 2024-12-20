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
            up, down, left, right = False, False, False, False
            region_res += 1
            
            if 0 <= index[0] + 1 < m_len:
                Q.put((index[0] + 1, index[1]))
                if (index[0] + 1, index[1]) not in region_index and m[index[0] + 1, index[1]] != plant:
                    down = True
            else:
                down = True
            
                
            if 0 <= index[0] - 1 < m_len:
                Q.put((index[0] - 1, index[1]))
                if (index[0] - 1, index[1]) not in region_index and m[index[0] - 1, index[1]] != plant:
                    up = True
            else:
                up = True
                
            if 0 <= index[1] + 1 < m_len:
                Q.put((index[0], index[1] + 1))
                if (index[0], index[1] + 1) not in region_index and m[index[0], index[1] + 1] != plant:
                    right = True
            else:
                right = True

            if 0 <= index[1] - 1 < m_len:
                Q.put((index[0], index[1] - 1))
                if (index[0], index[1] - 1) not in region_index and m[index[0], index[1] - 1] != plant:
                    left += True
            else:
                left = True

            #print(index)
            #print(f"UP: {up}, RIGHT: {right}, DOWN: {down}, LEFT: {left}")
            if up and right:
                perimeter += 1
            elif not (up or right) and m[index[0] - 1, index[1] + 1] != plant and (index[0] - 1, index[1] + 1) not in region_index:
                perimeter += 1
                
            if right and down:
                perimeter += 1
            elif not (right or down) and m[index[0] + 1, index[1] + 1] != plant and (index[0] + 1, index[1] + 1) not in region_index:
                perimeter += 1
                
            if down and left:
                perimeter += 1
            elif not (down or left) and m[index[0] + 1, index[1] - 1] != plant and (index[0] + 1, index[1] - 1) not in region_index:
                perimeter += 1
                
            if left and up:
                perimeter += 1
            elif not (left or up) and m[index[0] - 1, index[1] - 1] != plant and (index[0] - 1, index[1] - 1) not in region_index:
                perimeter += 1

            #print(perimeter)
            
    print("Perimeter: ")
    print(perimeter)
    print(region_res)
    return (region_res * perimeter)

for i in range(m_len):
    for j in range(m_len):
        plant = m[i][j]
        if plant != "#":
            res += check_region(i, j)

print(res)

