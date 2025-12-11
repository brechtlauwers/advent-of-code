import numpy as np
from functools import cache


with open("2025/day11/input.txt") as file_in:
    servers = dict()
    for line in file_in:
        l = line.strip().split()
        servers[l[0][:-1]] = l[1:]


@cache
def dfs(current, dest, depth, found_dac, found_fft):
    if current == dest:
        if found_dac and found_fft:
            return 1
        return 0

    if depth <= 0:
        return 0

    total_paths = 0

    for child in servers.get(current, []):
        is_dac = found_dac or (child == "dac")
        is_fft = found_fft or (child == "fft")
        total_paths += dfs(child, dest, depth - 1, is_dac, is_fft)
    return total_paths


count = dfs("svr", "out", 50, False, False)

print(count)
