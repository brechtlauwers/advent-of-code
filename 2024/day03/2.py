import re

with open("input.txt") as file_in:
    input = []
    for line in file_in:
        input.append(line)

l = []
res = 0

for string in input:
    l += re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", string)

active = True
    
for function in l:
    do = re.search("do\(\)", function)
    if do is not None:
        active = True

    dont = re.search("don\'t\(\)", function)
    if dont is not None:
        active = False
    
    num = re.search("\d+", function)
    if (num is not None) and active:
        n1, n2 = re.findall("\d+", function)
        res += int(n1) * int(n2)

    print(function)
    print(res)


print(res)
