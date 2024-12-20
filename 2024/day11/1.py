from functools import cache
from collections import Counter
import copy

with open("input.txt") as file_in:
    stones = []
    for line in file_in:
        stones += (line.split())

#stones = ['125', '17']
stones_dict = Counter(stones)

@cache
def blink_stone(stone):
    if stone == "0":
        return "1"
    elif len(stone) % 2 == 0:
        return [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
    else:
        return str(int(stone) * 2024)


for blinks in range(75):
    new_stones_dict = dict()
    
    for stone, amount in stones_dict.items():
        res = blink_stone(stone)
            
        if isinstance(res, list):
            new_stones_dict[res[0]] = new_stones_dict.get(res[0], 0) + amount
            new_stones_dict[res[1]] = new_stones_dict.get(res[1], 0) + amount
        else:
            new_stones_dict[res] = new_stones_dict.get(res, 0) + amount

    stones_dict = new_stones_dict
    
    print(f"Blink {blinks+1}:")
    print(sum(stones_dict.values()))
