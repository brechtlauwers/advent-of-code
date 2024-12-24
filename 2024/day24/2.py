import pprint
import graphviz
from itertools import combinations

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
    gate_dict = {}

    for v in values:
        val_dict[v[:3]] = int(v[-1])
    for g in gates:
        in1, op, in2, _, out = g.split()
        gate_dict[(in1, in2, op)] = out
    return val_dict, gate_dict

def operation(x, y, op):
    if op == "OR":
        return x or y
    elif op == "XOR":
        return x ^ y
    else:
        return x and y

def get_xy(values):
    x, y = "", ""
    for val, res in values.items():
        if val.startswith("x"):
            x += str(res)
        else:
            y += str(res)
    return x[::-1], y[::-1]

def get_final_val(values):
    final_res = ""
    for val, res in sorted(values.items()):
        if val.startswith("z"):
            final_res += str(res)
    return final_res[::-1]

def bin_to_int(binair):
    return int(binair, 2)

def get_output(values, gates):
    changed = True
    while changed:
        changed = False
        for gate in gates.items():
            in1, in2, op = gate[0]
            out = gate[1]
            if in1 in values and in2 in values and out not in values:
                res = operation(values[in1], values[in2], op)
                values[out] = res
                changed = True
    return values

def swap_4pairs(gates):
    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(gates)

def visualise(values, gates):
    dot = graphviz.Digraph()
    dot.attr(rankdir="LR", splines="polyline", ranksep="1.0")

    # Use a counter to make each operator unique
    operator_counter = {}

    for (in1, in2, op), out in gates.items():
        # Create a unique identifier for each operator
        if op not in operator_counter:
            operator_counter[op] = 0
        operator_counter[op] += 1
        unique_op = f"{op}_{operator_counter[op]}"  # e.g., "OR_1", "AND_2"

        # Add nodes with shapes and colors
        dot.node(in1, label=f"Input\n{in1}", shape="box", color="green", style="filled")
        dot.node(in2, label=f"Input\n{in2}", shape="box", color="green", style="filled")
        dot.node(unique_op, label=f"Operator\n{op}", shape="circle", color="red", style="filled")
        dot.node(out, label=f"Output\n{out}", shape="ellipse", color="blue", style="filled")

        # Add edges with labels
        dot.edge(in1, unique_op, label="input1")
        dot.edge(in2, unique_op, label="input2")
        dot.edge(unique_op, out, label="result")
    dot.render('graph', format='png')

values, gates = process_input(values, gates)
x, y = get_xy(values)
values = get_output(values, gates)
final_res = get_final_val(values)

visualise(values, gates)

res_int = int(final_res, 2)
x_int = int(x, 2)
y_int = int(y, 2)
print(f"Z: {res_int}")
print("0b" + final_res)
print(f"X + Y: {x_int + y_int}")
print(str(bin(bin_to_int(x) + bin_to_int(y))))
print(f"DONE??: {res_int == x_int + y_int}")

out_list = []
for gate, res in gates.items():
    out_list.append(res)

swaplist = sorted(["z14", "vss", "z31", "kpp", "z35", "sgj", "kdh", "hjf"])
print(','.join(swaplist))

#print(out_list)
#while bin_to_int(x) + bin_to_int(y) != bin_to_int(final_res):

#gates = swap_4pairs(gates)
#values, gates = process_input(values, gates)

#1011110001110011000110000011000001010101001000
#1011110001110011000101110011000001010101001000
