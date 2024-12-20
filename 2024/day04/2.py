import re

# XMAS occurs 18 times
test_input = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX', 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA', 'MAMMMXMMMM', 'MXMXAXMASX']

with open("input.txt") as file_in:
    input = []
    for line in file_in:
        input.append(line.strip())

res = 0
total_length = len(input)

for i in range(total_length - 2):
    for j in range(total_length - 2):
        if (input[i][j] == "M" and input[i][j+2] == "M" and
            input[i+1][j+1] == "A" and
            input[i+2][j] == "S" and input[i+2][j+2] == "S"):
            res += 1

        if (input[i][j] == "M" and input[i][j+2] == "S" and
            input[i+1][j+1] == "A" and
            input[i+2][j] == "M" and input[i+2][j+2] == "S"):
            res += 1

        if(input[i][j] == "S" and input[i][j+2] == "M" and
            input[i+1][j+1] == "A" and
            input[i+2][j] == "S" and input[i+2][j+2] == "M"):
            res +=1

        if(input[i][j] == "S" and input[i][j+2] == "S" and
            input[i+1][j+1] == "A" and
            input[i+2][j] == "M" and input[i+2][j+2] == "M"):
            res += 1
        

print(res)
