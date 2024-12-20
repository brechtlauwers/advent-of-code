import re

# XMAS occurs 18 times
test_input = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX', 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA', 'MAMMMXMMMM', 'MXMXAXMASX']

with open("input.txt") as file_in:
    input = []
    for line in file_in:
        input.append(line.strip())

res = 0
total_length = len(input)

# Vertical
input_vertical = []
for i in range(total_length):
    word = ""
    for j in range(total_length):
        word += input[j][i]
    input_vertical.append(word)

for i in range(total_length - 3):
    for j in range(total_length - 3):
        word = input[i][j] + input[i+1][j+1] + input[i+2][j+2] + input[i+3][j+3]
        if word == "XMAS" or word == "SAMX":
            res += 1

for i in range(total_length - 3):
    for j in range(total_length - 1, 2, -1):
        word = input[i][j] + input[i+1][j-1] + input[i+2][j-2] + input[i+3][j-3]
        print(word)
        if word == "XMAS" or word == "SAMX":
            res += 1

input += input_vertical
print(input)
    
# Horizontal, backwards and vertical search
for string in input:
    res += len(re.findall("XMAS", string))
    res += len(re.findall("XMAS", string[::-1]))


print(res)
