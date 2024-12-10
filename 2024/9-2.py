import itertools

example = """2333133121414131402"""

example = open("9.puzz", "r").read()
disk = []

def print_disk(disk):
    line = ""
    for f_id, blocks, blanks, extras in disk:
        line += str(f_id) * blocks + "." * (blanks + extras)
    print(line)

for f_id, chars in enumerate(itertools.batched(example, n=2)):
    disk.append([
        f_id,
        int(chars[0]),
        int(chars[1]) if len(chars) > 1 else 0,
        0
    ])

i = 0
j = len(disk) - 1
x = 0
while len(disk) > 0:

    if disk[i][2] >= disk[j][1]:
        disk[j-1][3] = disk[j][1] + disk[j][2]
        disk[j][2] = disk[i][2] - disk[j][1]
        disk[i][2] = 0
        disk = disk[:i+1] + [disk[j]] + disk[i+1:j] + disk[j+1:]
        j = len(disk) - 1
        i += 1
    else:
        i += 1
    if j <= i:
        i = 0
        j -= 1
    if j == 0:
        break

total = 0
i = 0
for f_id, blocks, blanks, extras in disk:
    for _ in range(blocks):
        total += i * f_id
        i += 1
    i += blanks + extras


print(total)
