with open("input.txt") as file_in:
    page_ordering, page_updates = [], []
    update = False
    for line in file_in:
        l = line.strip()
        if l == '':
            update = True
            continue
        
        if update:
            page_updates.append(l)
        else:
            page_ordering.append(l)

#page_ordering = ["47|53", "97|13", "97|61", "97|47", "75|29", "61|13", "75|53", "29|13", "97|29", "53|29", "61|53", "97|53", "61|29", "47|13", "75|47", "97|75", "47|61", "75|61", "47|29", "75|13", "53|13"]

#page_updates = ["75,47,61,53,29", "97,61,53,29,13", "75,29,13", "75,97,47,61,53", "61,13,29", "97,13,75,29,47"]

def check(i1, i2, l):
    for pages in page_ordering:
        p1, p2 = pages.split("|")

        if l[i1] == p2:
            if p1 in l[i1+1:]:
                return False
    return True

def correct(l):    
    for i in range(len(l) - 1):
        if not check(i, i+1, l):
            l[i], l[i+1] = l[i+1], l[i]

    for i in range(len(l) - 1):
        if not check(i, i+1, l):
            correct(l)
            break
    return l

res = 0

for page_update in page_updates:
    update_list = page_update.split(',')
    valid = True

    for i in range(len(update_list) - 1):
        if not check(i, i+1, update_list):
            valid = False
            break

    if not valid:
        update_list = correct(update_list)
        #print(update_list)
        res += int(update_list[len(update_list) // 2])


print(res)
