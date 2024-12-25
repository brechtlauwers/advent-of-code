with open("input.txt") as file_in:
    temp, res = [], []
    for line in file_in:
        if line == '\n':
            res.append(temp)
            temp = []
            continue
        temp += line.split()
    res.append(temp)


def process_input(res):
    locks, keys = [], []
    for x in res:
        counter = [0, 0, 0, 0, 0]
        for row in x[1:-1]:
            for i in range(5):
                if row[i] == "#":
                    counter[i] += 1
                    
        if x[0] == ".....":         # Locks
            locks.append(counter)
        else:
            keys.append(counter)
    return locks, keys

locks, keys = process_input(res)

counter = 0
for lock in locks:
    for key in keys:
        res = [sum(x) for x in zip(key, lock)]
        if max(res) <= 5:
            counter += 1
print(counter)
