import itertools
from collections import deque

example = """2333133121414131402"""

example = open("9.puzz", "r").read()
disk = deque()

for f_id, chars in enumerate(itertools.batched(example, n=2)):
    disk.append((
        f_id,
        int(chars[0]),
        int(chars[1]) if len(chars) > 1 else 0
    ))

new_disk = deque()
while len(disk) > 0:
    f_id, blocks, blanks = disk.popleft()
    sub_disk = deque()
    while blanks > 0 and len(disk) > 0:
        f_id2, blocks2, _ = disk.pop()
        moves = min(blanks, blocks2)
        blocks2 -= moves
        blanks -= moves
        sub_disk.append((f_id2, moves, 0))
        if blocks2 > 0:
            disk.append((f_id2, blocks2, 0))
    new_disk.append((f_id, blocks, blanks))
    new_disk.extend(sub_disk)

total = 0
i = 0
for f_id, blocks, blanks in new_disk:
    for _ in range(blocks):
        total += i * f_id
        i += 1


print(total)
