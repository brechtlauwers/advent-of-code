with open("2025/day01/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip())


start_dial = 50
amount_zero = 0

for line in lines:
    num = int(line[1:])
    if line[0] == "L":
        start_dial = (start_dial - num) % 100
    else:  # R
        start_dial = (start_dial + num) % 100

    if start_dial == 0:
        amount_zero += 1

print(amount_zero)
