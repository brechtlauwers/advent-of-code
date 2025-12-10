import numpy as np
import itertools
from functools import cache


with open("2025/day10/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip().split())


def merge_buttons(b1, b2):
    return tuple(list(set(b1) ^ set(b2)))


@cache
def press_buttons(buttons):
    if len(buttons) == 1:
        return buttons[0]
    if len(buttons) == 2:
        return merge_buttons(buttons[0], buttons[1])

    new_button = merge_buttons(buttons[0], buttons[1])
    return press_buttons(tuple([new_button]) + buttons[2:])


res = 0

for line in lines:
    # Input processing
    machine = []
    for char in list(line[0])[1:-1]:
        if char == ".":
            machine.append(0)
        else:
            machine.append(1)
    machine = tuple(i for i, val in enumerate(machine) if val == 1)

    buttons = []
    for b in list(line[1:-1]):
        b = b.split(',')
        b[0] = b[0][1]
        b[-1] = b[-1][0]
        buttons.append(tuple(int(c) for c in b))
    buttons = list(buttons)

    # The algorithm
    stop = False
    for press in range(1, len(buttons)):
        # All combinations of buttons with 'press' amount of buttons
        for pressed_buttons in itertools.combinations(buttons, press):
            button_res = press_buttons(pressed_buttons)
            if button_res == machine:
                stop = True
                break
        if stop:
            res += press
            break

print(res)
