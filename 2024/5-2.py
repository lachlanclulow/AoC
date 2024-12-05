from functools import cmp_to_key

example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

example = open("5.puzz", "r").read()

input = example.split("\n\n")
rules = input[0].splitlines()
updates = input[1].splitlines()

from_set = {}
to_set = {}

for rule in rules:
    from_, to_ = rule.split("|")
    if from_ not in from_set:
        from_set[from_] = {to_}
    else:
        from_set[from_] |= {to_}
    if to_ not in to_set:
        to_set[to_] = {from_}
    else:
        to_set[to_] |= {from_}

def order(a, b):
    if a in to_set and b in to_set[a] or b in from_set and a in from_set[b]:
        return 1
    if a in from_set and b in from_set[a] or b in to_set and a in to_set[b]:
        return -1
    return 0

total = 0

for update in updates:
    pages = update.split(',')
    sorted_pages = sorted(pages, key=cmp_to_key(order))
    if pages != sorted_pages:
        total += int(sorted_pages[len(sorted_pages)//2])

print(total)