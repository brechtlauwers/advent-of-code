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

K = 1000  # number of pairs to connect
for _, i, j in distances[:K]:
    uf.unite(i, j)

groups = uf.groups()
groups.sort(key=len, reverse=True)

res = 1
for g in groups[:3]:
    res *= len(g)

print(res)
