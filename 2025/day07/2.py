import numpy as np
import functools


with open("2025/day07/input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append([x for x in line.strip()])
    lines = np.array(lines)

start_idx = np.where(lines[0] == "S")[0][0]
max_len = lines.shape[0]

splits = dict()
for i in range(1, max_len):
    splits[i] = np.where(lines[i] == "^")[0]


@functools.cache
def get_amount(i, beam_idx):
    if i >= max_len:  # Stop recursion
        return 1

    if i % 2 == 1:  # no splits here
        return get_amount(i + 1, beam_idx)

    if beam_idx in splits[i]:
        return (
            get_amount(i + 1, beam_idx - 1)
            + get_amount(i + 1, beam_idx + 1)
        )
    else:
        return get_amount(i + 1, beam_idx)


print(get_amount(1, start_idx))
