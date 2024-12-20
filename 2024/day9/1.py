with open("input.txt") as file_in:
    disk_map = file_in.read().strip('\n')

disk_map_example = "2333133121414131402"

def disk_representation(disk_map):
    rep = []
    for i in range(1, len(disk_map), 2):
        # i-1 = block, i = free space
        block = i-1
        free_space = disk_map[i]
        block_file = disk_map[block]
        block_id = (i-1) // 2

        for place in range(int(block_file)):
            rep.append(block_id)
        for free_place in range(int(free_space)):
            rep.append(".")

    for place in range(int(disk_map[-1])):
        rep.append(len(disk_map) // 2)
    
    return(rep)

def next_free_index(rep, current_i):
    for i in range(current_i, len(rep)):
        if rep[i] == ".":
            return i

#rep = disk_representation(disk_map_example)
rep = disk_representation(disk_map)

current_i = 0
for i in range(len(rep)-1, -1, -1):
    symbol = rep[i]
    if not symbol == ".":
        current_i = next_free_index(rep, current_i)
        if current_i >= i:
            break
        rep[current_i] = symbol
        rep[i] = "."

res = 0
for i in range(len(rep)):
    if not rep[i] == ".":
        res += int(rep[i]) * i

print(res)
