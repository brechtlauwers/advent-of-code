from collections import defaultdict

with open("input.txt") as file_in:
    values = []
    gates = []
    wl = False
    for line in file_in:
        if line == '\n':
            wl = True
            continue
        if wl:
            gates.append(line.strip())
        else:
            values.append(line.strip())

def process_input(values, gates):
    val_dict = {}
    gate_dict = defaultdict(list)
    
    for v in values:
        val_dict[v[:3]] = int(v[-1])
    for g in gates:
        in1, op, in2, _, out = g.split()
        gate_dict[(in1, in2, op)].append(out)
    return val_dict, gate_dict

def operation(x, y, op):
    if op == "OR":
        return x or y
    elif op == "XOR":
        return x ^ y
    else:
        return x and y


values, gates = process_input(values, gates)
changed = True

while changed:
    changed = False
    for gate in gates.items():
        in1, in2, op = gate[0]
        outs = gate[1]
        
        for out in outs:
            if in1 in values and in2 in values and out not in values:
                res = operation(values[in1], values[in2], op)
                values[out] = res
                changed = True

final_res = ""
for val, res in sorted(values.items()):
    if val.startswith("z"):
        final_res += str(res)

print(int(final_res[::-1], 2))
