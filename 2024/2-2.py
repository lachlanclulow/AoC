example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def check_safe(l):
    asc = None
    asc = set()
    diffs = set()
    for i in range(1, len(l)):
        d = int(l[i]) - int(l[i-1])
        diffs |= {d}
        asc |= {d > 0}

    if len(diffs - {-1, -2, -3}) == 0 or len(diffs - {1, 2, 3}) == 0:
        print(f"{l}, {diffs}, {asc}")
        return 1
    
    return 0

example = open("2.puzz", "r").read()
safe = 0

for line in example.splitlines():
    vals = line.split(" ")
    if check_safe(vals):
        safe += 1
    else:
        for i in range(len(vals)):
            if check_safe(vals[:i] + vals[i+1:]):
                safe += 1
                break

print(safe)