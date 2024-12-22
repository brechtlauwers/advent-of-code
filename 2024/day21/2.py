from queue import Queue
from itertools import permutations
from functools import cache
from itertools import pairwise



with open("input.txt") as file_in:
    codes = []
    for line in file_in:
        codes.append(line.strip())

# num_keypad = {'0': [('A', '>'), ('2', '^')],
#               'A': [('0', '<'), ('3', '^')],
#               '1': [('2', '>'), ('4', '^')],
#               '2': [('1', '<'), ('5', '^'), ('3', '>'), ('0', 'v')],
#               '3': [('2', '<'), ('6', '^'), ('A', 'v')],
#               '4': [('5', '>'), ('7', '^'), ('1', 'v')],
#               '5': [('4', '<'), ('8', '^'), ('2', 'v'), ('6', '>')],
#               '6': [('5', '<'), ('9', '^'), ('3', 'v')],
#               '7': [('8', '>'), ('4', 'v')],
#               '8': [('7', '<'), ('5', 'v'), ('9', '>')],
#               '9': [('8', '<'), ('6', 'v')],
#               'A': [('0', '<'), ('3', '^')]}

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
direct_keypad = {('<', 'v'): ['>'],
                 ('<', '^'): ['>^'],
                 ('<', '>'): ['>>'],
                 ('<', 'A'): ['>^>', '>>^'],
                 ('<', '<'): [''],
                 ('v', '<'): ['<'],
                 ('v', '^'): ['^'],
                 ('v', '>'): ['>'],
                 ('v', 'A'): ['>^', '^>'],
                 ('v', 'v'): [''],
                 ('>', 'A'): ['^'],
                 ('>', 'v'): ['<'],
                 ('>', '<'): ['<<'],
                 ('>', '^'): ['<^', '^<'],
                 ('>', '>'): [''],
                 ('^', '<'): ['v<'],
                 ('^', 'v'): ['v'],
                 ('^', 'A'): ['>'],
                 ('^', '>'): ['>v', 'v>'],
                 ('^', '^'): [''],
                 ('A', '^'): ['<'],
                 ('A', '>'): ['v'],
                 ('A', 'v'): ['<v', 'v<'],
                 ('A', '<'): ['<v<'],
                 ('A', 'A'): ['']}

direct_keypad = {'A': {'A': 'A', '<': 'v<<A', '^': '<A', '>': 'vA', 'v': '<vA'},'<': {'A': '>>^A', '<': 'A', '^': '>^A', '>': '>>A', 'v': '>A'},'^': {'A': '>A', '<': 'v<A', '^': 'A', '>': 'v>A', 'v': 'vA'},'>': {'A': '^A', '<': '<<A', '^': '<^A', '>': 'A', 'v': '<A'},'v': {'A': '^>A', '<': '<A', '^': '^A', '>': '>A', 'v': 'A'}}


def enter_code(code):
    code = "A" + code
    path = ""
    for i in range(len(code) - 1):
        path += num_keypad[code[i]][code[i+1]]
    return path

# def enter_direct_code(code):
#     code = "A" + code
#     path = ""
#     for i in range(len(code) - 1):
#         path += direct_keypad[code[i]][code[i+1]]
#     return path

def enter_direct_code(code):
    code = "A" + code
    n = len(code)
    result = bytearray()  # Use a bytearray for efficient string concatenation
    append = result.extend  # Avoid attribute lookups in the loop

    for i in range(n - 1):
        append(direct_keypad[code[i]][code[i + 1]].encode())

    return result.decode()

total = 0
for code in codes:
    direct_code = enter_code(code)
    
    for _ in range(25):
        direct_code = enter_direct_code(direct_code)
        print(_, len(direct_code))
        
    print(f"{code}: {final_code}")
    code_len = len(final_code)
    num_part = int(code[:3])
    print(code_len, num_part)
    
    total += code_len * num_part

print(total)


