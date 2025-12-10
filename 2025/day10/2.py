import numpy as np
import itertools
from functools import cache
from collections import defaultdict
from scipy.optimize import linprog


with open("2025/day10/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip().split())

res = 0

for line in lines:
    # Input processing
    joltages = [int(x) for x in line[-1][1:-1].split(',')]

    buttons = []
    for b in list(line[1:-1]):
        counter = [0 for _ in range(len(joltages))]
        b = b.split(',')
        b[0] = b[0][1]
        b[-1] = b[-1][0]
        for c in b:
            counter[int(c)] = 1
        buttons.append(tuple(counter))

    # The algorithm
    stop = False
    press = 0
    amount_buttons = len(buttons)

    # Integer programming
    A = np.zeros((len(joltages), amount_buttons))
    for i in range(len(joltages)):
        for j in range(amount_buttons):
            if buttons[j][i] == 1:
                A[i][j] = 1
    b = joltages
    c = [1 for _ in range(amount_buttons)]

    lin_res = linprog(c, A_eq=A, b_eq=b, integrality=c)
    res += lin_res.fun

print(int(res))
