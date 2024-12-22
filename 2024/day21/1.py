with open("input.txt") as file_in:
    codes = []
    for line in file_in:
        codes.append(line.strip())

num_keypad = {'A': {'A': 'A', '0': '<A', '1': '^<<A', '2': '<^A', '3': '^A', '4': '^^<<A', '5': '<^^A', '6': '^^A', '7': '^^^<<A', '8': '<^^^A', '9': '^^^A'},
 '0': {'A': '>A', '0': 'A', '1': '^<A', '2': '^A', '3': '^>A', '4': '^^<A', '5': '^^A', '6': '^^>A', '7': '^^^<A', '8': '^^^A', '9': '^^^>A'},
 '1': {'A': '>>vA', '0': '>vA', '1': 'A', '2': '>A', '3': '>>A', '4': '^A', '5': '^>A', '6': '^>>A', '7': '^^A', '8': '^^>A', '9': '^^>>A'},
 '2': {'A': 'v>A', '0': 'vA', '1': '<A', '2': 'A', '3': '>A', '4': '<^A', '5': '^A', '6': '^>A', '7': '<^^A', '8': '^^A', '9': '^^>A'},
 '3': {'A': 'vA', '0': '<vA', '1': '<<A', '2': '<A', '3': 'A', '4': '<<^A', '5': '<^A', '6': '^A', '7': '<<^^A', '8': '<^^A', '9': '^^A'},
 '4': {'A': '>>vvA', '0': '>vvA', '1': 'vA', '2': 'v>A', '3': 'v>>A', '4': 'A', '5': '>A', '6': '>>A', '7': '^A', '8': '^>A', '9': '^>>A'},
 '5': {'A': 'vv>A', '0': 'vvA', '1': '<vA', '2': 'vA', '3': 'v>A', '4': '<A', '5': 'A', '6': '>A', '7': '<^A', '8': '^A', '9': '^>A'},
 '6': {'A': 'vvA', '0': '<vvA', '1': '<<vA', '2': '<vA', '3': 'vA', '4': '<<A', '5': '<A', '6': 'A', '7': '<<^A', '8': '<^A', '9': '^A'},
 '7': {'A': '>>vvvA', '0': '>vvvA', '1': 'vvA', '2': 'vv>A', '3': 'vv>>A', '4': 'vA', '5': 'v>A', '6': 'v>>A', '7': 'A', '8': '>A', '9': '>>A'},
 '8': {'A': 'vvv>A', '0': 'vvvA', '1': '<vvA', '2': 'vvA', '3': 'vv>A', '4': '<vA', '5': 'vA', '6': 'v>A', '7': '<A', '8': 'A', '9': '>A'},
 '9': {'A': 'vvvA', '0': '<vvvA', '1': '<<vvA', '2': '<vvA', '3': 'vvA', '4': '<<vA', '5': '<vA', '6': 'vA', '7': '<<A', '8': '<A', '9': 'A'}}

# All possible mappings for (from, to): path
direct_keypad = {'A': {'A': 'A', '<': 'v<<A', '^': '<A', '>': 'vA', 'v': '<vA'},'<': {'A': '>>^A', '<': 'A', '^': '>^A', '>': '>>A', 'v': '>A'},'^': {'A': '>A', '<': 'v<A', '^': 'A', '>': 'v>A', 'v': 'vA'},'>': {'A': '^A', '<': '<<A', '^': '<^A', '>': 'A', 'v': '<A'},'v': {'A': '^>A', '<': '<A', '^': '^A', '>': '>A', 'v': 'A'}}

def enter_code(code):
    code = "A" + code
    paths = []
    for i in range(len(code) - 1):
        path_steps = num_keypad[code[i]][code[i+1]]
        paths += [path_steps]
    return ''.join(paths)

def enter_direct_code(code):
    code = "A" + code
    paths = []
    for i in range(len(code) - 1):
        path_steps = direct_keypad[code[i]][code[i+1]]
        paths += [path_steps]
    return ''.join(paths)

#codes = ["029A", "980A", "179A", "456A", "379A"]
#codes = ["379A"]

total = 0
for code in codes:
    direct_code = enter_code(code)
    direct_code = enter_direct_code(direct_code)
    final_code = enter_direct_code(direct_code)

    print(f"{code}: {final_code}")
    code_len = len(final_code)
    num_part = int(code[:3])
    print(code_len, num_part)
    
    total += code_len * num_part

# 278748
print(total)


