import numpy as np


with open("2025/day11/input.txt") as file_in:
    servers = dict()
    for line in file_in:
        l = line.strip().split()
        servers[l[0][:-1]] = l[1:]


def dfs(src, dest, path, all_paths):
    path.append(src)

    if src == dest:
        all_paths.append(path.copy())
    else:
        for child in servers[src]:
            dfs(child, dest, path, all_paths)

    path.pop()


all_paths = []

dfs("you", "out", [], all_paths)
print(len(all_paths))
