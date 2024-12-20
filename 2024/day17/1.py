with open("input.txt") as file_in:
    registers = []
    program = ""
    movements = False
    for line in file_in:
        if line == '\n':
            movements = True
            continue
        if movements:
            program = line.strip()[9:].split(',')
        else:
            registers.append(line.strip()[12:])

## TEST INPUT
#program = "0,1,5,4,3,0".split(',')
#registers = ['729', '0', '0']

reg_a = int(registers[0])
reg_b = int(registers[1])
reg_c = int(registers[2])

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
        reg_a = int(reg_a / pow(2, combo_operand))
    if opcode == 1:             # bitwise XOR
        reg_b = reg_b ^ operand
    if opcode == 2:             # mod 8
        reg_b = combo_operand % 8
    if opcode == 3 and reg_a != 0:  # jump ip
        ip = operand - 2
    if opcode == 4:             # bitwise XOR
        reg_b = reg_b ^ reg_c
    if opcode == 5:             # out!
        out.append(combo_operand % 8)
    if opcode == 6:
        reg_b = int(reg_a / pow(2, combo_operand))
    if opcode == 7:
        reg_c = int(reg_a / pow(2, combo_operand))

    ip += 2
    
print(','.join([str(el) for el in out]))
