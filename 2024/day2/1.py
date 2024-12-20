import numpy as np

with open("input.txt") as file_in:
    reports = []
    for line in file_in:
        n = [int(x) for x in line.split()]
        reports.append(n)

safe_counter = 0

def descending(report):
    global safe_counter
    safe = True
    
    for i in range(len(report) - 1):
        if report[i] <= report[i+1] or report[i] > report[i+1] + 3:
            safe = False

    if safe:
        safe_counter += 1


def ascending(report):
    global safe_counter
    safe = True

    for i in range(len(report) - 1):
        if report[i] >= report[i+1] or report[i] + 3 < report[i+1]:
            safe = False

    if safe:
        safe_counter += 1


for report in reports:
    if report[0] > report[1]:
        descending(report)
    elif report[0] < report[1]:
        ascending(report)

print(safe_counter)


