import re

with open("input.txt") as file_in:
    input = []
    for line in file_in:
        input.append(line)

test_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

l = []
res = 0

for string in input:
    l += re.findall("mul\(\d+,\d+\)", string)

for mul in l:
    n1, n2 = re.findall("\d+" ,mul)
    res += int(n1) * int(n2)

print(res)
