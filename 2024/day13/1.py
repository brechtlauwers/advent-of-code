import re
import numpy as np
from scipy.optimize import linprog

with open("input.txt") as file_in:
    l = []
    for line in file_in:
        l.append(line.strip())



example_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

#l = []
#for line in example_input.splitlines():
#    l.append(line)

total = 0
for i in range(0, len(l), 4):
    button_a = l[i]
    button_b = l[i+1]
    prize = l[i+2]

    a_1, a_2 = re.findall(r"\d+", button_a)
    b_1, b_2 = re.findall(r"\d+", button_b)
    res_1, res_2 = re.findall(r"\d+", prize)

    c = np.array([3, 1])        # Coefficients for objective function
    A = np.array([[a_1, b_1],
                  [a_2, b_2]], dtype=np.int32)   # Equality constraint matrix
    b = np.array([res_1, res_2], dtype=np.int32)  # Equality constraint vector
    
    bounds = [(0, 100), (0, 100)]   # x,y bounds (min, max)
    result = linprog(c, A_eq=A, b_eq=b, bounds=bounds, integrality=[1,1]).fun

    if result:
        total += result

print(total)
