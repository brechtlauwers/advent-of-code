from functools import cache
with open("input.txt") as file_in:
    towels = []
    patterns = []
    wl = False
    for line in file_in:
        if line == '\n':
            wl = True
            continue
        if wl:
            patterns.append(line.strip())
        else:
            towels += (line.strip().split(', '))

#towels = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
#patterns = ['brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb']

valids = set()

@cache
def recursive_match(pattern):
    p_len = len(pattern)
    
    if p_len == 0:
        return 1

    matching = []
    
    for towel in towels:
        towel_len = len(towel)
        if towel_len <= p_len:
            new_pattern = pattern[:towel_len]
            if new_pattern == towel:
                matching.append(pattern[towel_len:])

    if len(matching) == 0:
        return 0
    
    return sum(recursive_match(m) for m in matching)


total = 0
for pattern in patterns:
    res = recursive_match(pattern)
    if res > 0:
        total += 1
        
print(total)

