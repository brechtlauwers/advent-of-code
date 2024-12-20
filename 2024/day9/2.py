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

def get_free_size(rep, current_i, min_len):
    max_res = 0
    max_i = 0
    res = 0
    for j in range(0, current_i):
        if rep[j] == ".":
            res += 1
        else:
            res = 0
            
        if max_res < res:
            max_res = res
            max_i = j - res + 1
            if max_res == min_len:
                return max_i, max_res
    return False, False

def get_file_size(rep, current_i):
    res = 0
    symbol = rep[current_i]
    for j in range(current_i, 0, -1):
        if rep[j] == symbol:
            res += 1
        else:
            return res

#rep = disk_representation(disk_map_example)
rep = disk_representation(disk_map)

current_i = 0
skip_symbol = set()
blacklist = []
for i in range(len(rep)-1, -1, -1):
    symbol = rep[i]
        
    if (not symbol == ".") and (not symbol in skip_symbol):
        current_i = next_free_index(rep, current_i)
        file_size = get_file_size(rep, i)
        max_free_i, free_size = get_free_size(rep, i, file_size)

        if file_size == None:
            break

        if free_size >= file_size:
            for free_i in range(file_size):
                rep[max_free_i + free_i] = symbol
                rep[i - free_i] = "."
        else:
            skip_symbol.add(symbol)
        
res = 0
for i in range(len(rep)):
    if not rep[i] == ".":
        res += int(rep[i]) * i

print(res)
#print(rep)
