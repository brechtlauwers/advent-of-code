from functools import cache

with open("input.txt") as file_in:
    registers = []
    program = ""
    movements = False
    for line in file_in:
        if line == '\n':
            movements = True
            continue
        if movements:
            program = [int(x) for x in line.strip()[9:].split(',')]
        else:
            registers.append(line.strip()[12:])

## TEST INPUT
#program = [int(x) for x in "0,3,5,4,3,0".split(',')]
#registers = ['2024', '0', '0']


#reg_a = int(registers[0])
reg_b = int(registers[1])
reg_c = int(registers[2])

@cache
def division(reg_a, combo_operand):
    return int(reg_a / pow(2, combo_operand))

@cache
def bitwiseXOR(a, b):
    return a ^ b

@cache
def mod_8(a):
    return a % 8

def run_program(program, reg_a, reg_b, reg_c):
    ip = 0
    out = []
    while ip < len(program):
        opcode = int(program[ip])
        operand = int(program[ip + 1])

        if 0 <= operand <= 3:
            combo_operand = operand
        if operand == 4:
            combo_operand = reg_a
        elif operand == 5:
            combo_operand = reg_b
        elif operand == 6:
            combo_operand = reg_c

        # Perform the instruction
        if opcode == 0:             # division
            reg_a = division(reg_a, combo_operand)
        if opcode == 1:             # bitwise XOR
            reg_b = bitwiseXOR(reg_b, operand)
        if opcode == 2:             # mod 8
            reg_b = mod_8(combo_operand)
        if opcode == 3 and reg_a != 0:  # jump ip
            ip = operand - 2
        if opcode == 4:             # bitwise XOR
            reg_b = bitwiseXOR(reg_b, reg_c)
        if opcode == 5:             # out!
            out.append(mod_8(combo_operand))
        if opcode == 6:
            reg_b = division(reg_a, combo_operand)
        if opcode == 7:
            reg_c = division(reg_a, combo_operand)
        ip += 2

    #print(reg_a, reg_b, reg_c)
    return out


def reverse_program(program, out):
    ip = len(program)
    reg_a, reg_b, reg_c = 0, 0, 0
    opcode = int(program[ip - 2])
    operand = int(program[ip - 1])
    
    while ip <= 0:
        pass


    ip -= 2

out = []
#reg_a = 35_000_000_000_000
reg_a = 164540892147300
#reg_a = 2
#reg_a = 282_000_000_000_000

while out != program:
    out = run_program(program, reg_a, reg_b, reg_c)
    print(reg_a, out)
    reg_a += 1

print(program)

print(run_program(program, 164540892147389, 0, 0))


#print(reg_a)


def step(A):
    B = A % 8
    B = B ^ 1
    C = A // (2**B)
    B = B ^ B
    B = B ^ C
    A = A / 8
    return B % 8
