import numpy as np
from unionfind import unionfind

with open("2025/day08/input.txt") as f:
    points = [tuple(map(int, line.split(','))) for line in f]

N = len(points)
points = np.array(points)
distances = []

for i in range(N):
    for j in range(i + 1, N):
        d = np.linalg.norm(points[i] - points[j])
        distances.append((d, i, j))

distances.sort(key=lambda x: x[0])

uf = unionfind(N)

for _, i, j in distances:
    uf.unite(i, j)
    if len(uf.groups()) == 1:
        print(points[i][0] * points[j][0])
        break
