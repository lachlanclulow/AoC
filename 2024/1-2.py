example = '''3   4
4   3
2   5
1   3
3   9
3   3
'''

list_1 = []
m = {}

with open("./1.puzz", "r") as f:

    for line in f.readlines():
        items = line.split("   ")
        list_1.append(int(items[0]))

        if int(items[1]) not in m:
            m[int(items[1])] = 1
        else:
            m[int(items[1])] += 1

s = 0

for n in list_1:
    if n in m:
        s += n * m[n]

print(s)