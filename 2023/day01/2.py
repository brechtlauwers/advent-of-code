import re

with open("2023/day01/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip())

digit_names = ["one", "two", "three", "four", "five",
               "six", "seven", "eight", "nine"]

inverted_names = [x[::-1] for x in digit_names]

res = 0

for line in lines:
    d1, d2 = 0, 0
    for i in range(len(line)):
        if line[i].isdigit():
            d1 = int(line[i])

        for list_i, digit in enumerate(digit_names):
            if line[i:].startswith(digit):
                d1 = list_i + 1

        if d1 != 0:
            break

    line = line[::-1]  # reverse the line
    for i in range(len(line)):
        if line[i].isdigit():
            d2 = int(line[i])

        for list_i, digit in enumerate(inverted_names):
            if line[i:].startswith(digit):
                d2 = list_i + 1

        if d2 != 0:
            break

    res += int(str(d1) + str(d2))

print(res)
