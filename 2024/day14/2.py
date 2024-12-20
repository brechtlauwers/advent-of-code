import re
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

with open("input.txt") as file_in:
    l = []
    for line in file_in:
        l.append(line.strip())

example_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

# l = []
# for line in example_input.splitlines():
#    l.append(line)

pos_list, vel_list = [], []
for robot in l:
    res = re.findall(r"-?\d+", robot)
    pos_list.append((int(res[0]), int(res[1])))
    vel_list.append((int(res[2]), int(res[3])))

x_len, y_len = 101, 103
#x_len, y_len = 11, 7

def safety_factor(pos_list):
    q1, q2, q3, q4 = 0, 0, 0, 0
    x_split = x_len // 2
    y_split = y_len // 2

    for pos in pos_list:
        x, y = pos[0], pos[1]
        if x == x_split or y == y_split:
            continue
    
        if x < x_split and y < y_split:
            q1 += 1
        elif x < x_split and y > y_split:
            q2 += 1
        elif x > x_split and y < y_split:
            q3 += 1
        else:
            q4 += 1

    return (q1, q2, q3, q4)

def visualise(m):
    for row in m:
        for el in row:
            if el != 0:
                print("#", end=",")
            else:
                print(".", end=",")
        print()

def check_line(pos_list):
    m = np.zeros(shape=(x_len, y_len))
    for pos in pos_list:
        m[pos] = 1

    vis = False

    for row in m:
        if sum(row) == 34:      # Found with >= 30 and print all those possibilities
            vis = True

    if vis:
        visualise(m)  
    

q1, q2, q3, q4 = 0, 0, 0, 1
counter = 0

while not q1 == q2 == q3 == q4:
    new_pos_list = []
    for i in range(len(pos_list)):
        pos = (pos_list[i][0], pos_list[i][1])

        new_x_pos = (pos[0] + vel_list[i][0]) % x_len
        new_y_pos = (pos[1] + vel_list[i][1]) % y_len

        new_pos_list.append((new_x_pos, new_y_pos))

    pos_list = new_pos_list

    print(counter)
    counter += 1
    check_line(pos_list)
    #visualise(pos_list)
    q1, q2, q3, q4 = safety_factor(pos_list)

print(pos_list)
print(safety_factor(pos_list))
