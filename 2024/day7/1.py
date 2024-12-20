from itertools import product, zip_longest
import operator

with open("input.txt") as file_in:
    l = []
    for line in file_in:
        l.append(line.split())


example_string = ["190: 10 19\n", "3267: 81 40 27\n", "83: 17 5\n", "156: 15 6\n", "7290: 6 8 6 15\n", "161011: 16 10 13\n", "192: 17 8 14\n", "21037: 9 7 18 13\n", "292: 11 6 16 20\n"]

#l = []
#for line in example_string:
#    l.append(line.split())

total_result = 0
    
for line in l:
    test_value = int(line[0][:-1])
    combinations = product('+*|', repeat=len(line) - 2)
    
    
    for comb in combinations:
        c = []
        for x, y in zip_longest(line[1:], comb):
            c += [x, y]

        ops = { "+": operator.add, "*": operator.mul, "|": operator.concat}

        res = c[0]
        for i in range(1, len(c[:-1]) - 1, 2):
            if c[i] == "+" or c[i] == "*":
                res = ops[c[i]](int(res), int(c[i+1]))
            if c[i] == "|":
                res = int(ops[c[i]](str(res), str(c[i+1])))
            if res > test_value:
                break

                
        if res == test_value:
            total_result += res
            break

print(total_result)

