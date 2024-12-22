from functools import cache
from collections import Counter

with open("input.txt") as file_in:
    codes = []
    for line in file_in:
        codes.append(line.strip())


@cache
def mix(code, secret):
    return code ^ secret

@cache
def prune(code):
    return code % 16777216

@cache
def compute_code(initial_code):
    secret_number = int(initial_code)

    # Part 1
    result = secret_number * 64
    secret_number = mix(secret_number, result)
    secret_number = prune(secret_number)

    # Part 2
    result = secret_number // 32
    secret_number = mix(secret_number, result)
    secret_number = prune(secret_number)

    # Part 3
    result = secret_number * 2048
    secret_number = mix(secret_number, result)
    secret_number = prune(secret_number)
    
    return secret_number

#codes = ["1", "2", "3", "2024"]
#codes = ["123"]

dict_list = []

for code in codes:
    res = code
    prev = int(str(code)[-1])
    price_change = []
    dict = {}
    
    for i in range(2001):
        res = compute_code(res)

        new = int(str(res)[-1])
        price = new - prev

        if i >= 4:
            pattern = tuple(price_change[i-4:i])
            if pattern not in dict.keys():
                dict[pattern] = prev

        prev = new
        price_change.append(price)

    dict_list.append(dict)

res = [Counter(x) for x in dict_list]



d = res[0]
for x in res[1:]:
    d += x

largest = max(d, key=d.get)

print(largest)
print(d[largest])


