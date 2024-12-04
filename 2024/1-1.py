example = '''3   4
4   3
2   5
1   3
3   9
3   3
'''

list_1 = []
list_2 = []

with open("./1.puzz", "r") as f:

    for line in f.readlines():
        items = line.split("   ")
        list_1.append(int(items[0]))
        list_2.append(int(items[1]))

    list_1.sort()
    list_2.sort()

    s = 0

    for a, b in zip(list_1, list_2):
        s += abs(a - b)

    print(s)