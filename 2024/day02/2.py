import numpy as np

with open("input.txt") as file_in:
    reports = []
    for line in file_in:
        n = [int(x) for x in line.split()]
        reports.append(n)


def correct_descending(report):
    safe = True
    for i in range(len(report) - 1):
        if report[i] <= report[i+1] or report[i] > report[i+1] + 3:
            safe = False
            break
    return safe


def correct_ascending(report):
    safe = True
    for i in range(len(report) - 1):
        if report[i] >= report[i+1] or report[i] + 3 < report[i+1]:
            safe = False
            break
    return safe


def damp(report):
    for i in range(len(report)):
        damp_report = report.copy()
        del damp_report[i]
        if check_ascending(damp_report):
            if correct_ascending(damp_report):
                return True
        elif check_descending(damp_report):
            if correct_descending(damp_report):
                return True

def check_ascending(a):
    return all(a[i] < a[i + 1] for i in range(len(a) - 1))
    
def check_descending(b):
    return all(b[i] > b[i + 1] for i in range(len(b) - 1))

safe_counter = 0

for report in reports:
    if check_ascending(report):
        if correct_ascending(report):
            safe_counter += 1
            continue
    elif check_descending(report):
        if correct_descending(report):
            safe_counter += 1
            continue

    if damp(report):
        safe_counter += 1


print(safe_counter)

# Answer should be 604
