with open("2025/day01/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip())


start_dial = 50
amount_zero = 0

for line in lines:
    num = int(line[1:])

    if line[0] == "L":
        res_num = start_dial - num

        if start_dial == 0:
            amount_zero -= 1

        if res_num < 0:
            amount_zero += abs(res_num // 100)

        if (res_num % 100) == 0:
            amount_zero += 1

        start_dial = res_num % 100

    else:  # R
        res_num = start_dial + num

        if res_num > 99:
            amount_zero += res_num // 100
        start_dial = res_num % 100

print(amount_zero)
