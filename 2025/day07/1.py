import numpy as np


with open("2025/day07/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append([x for x in line.strip()])
    lines = np.array(lines)

start_idx = np.where(lines[0] == "S")[0][0]
max_len = lines.shape[0]

beams = np.zeros(lines.shape[1])
beams[start_idx] = 1
res = 0

for depth_i in range(1, max_len):
    splits = np.where(lines[depth_i] == "^")[0]

    for num in splits:
        if beams[num] == 1:
            beams[num] = 0
            beams[num + 1] = 1
            beams[num - 1] = 1
            res += 1

print(res)
