import re

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
p=3,0 v=-1,-2
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

print(pos_list)
print(vel_list)

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

    return (q1 * q2 * q3 * q4)

for second in range(100):
    new_pos_list = []
    for i in range(len(pos_list)):
        pos = (pos_list[i][0], pos_list[i][1])

        new_x_pos = (pos[0] + vel_list[i][0]) % x_len
        new_y_pos = (pos[1] + vel_list[i][1]) % y_len

        new_pos_list.append((new_x_pos, new_y_pos))

    pos_list = new_pos_list

print(pos_list)


print(safety_factor(pos_list))
