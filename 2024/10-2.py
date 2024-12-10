from itertools import chain

example = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

example = open("10.puzz", "r").read()

grid = []

trailheads = []

height = len(example.splitlines())
width = len(example.splitlines()[0])

for y, line in enumerate(example.splitlines()):
    grid.append(list(line))
    for x, cell in enumerate(line):
        if cell == "0":
            trailheads.append((x, y))

def follow_trail(pos, elevation, grid, path=set()):
    x, y = pos
    if x < 0 or x >= width or y < 0 or y >= height:
        return set()
    
    new_elevation = int(grid[y][x])
    if new_elevation - elevation != 1:
        return set()

    if new_elevation == 9:
        return {(x, y)}
    
    return list(chain.from_iterable(follow_trail((x2, y2), new_elevation, grid, path|{(x, y)}) for x2, y2 in {(x-1, y), (x+1, y), (x, y-1), (x, y+1)} - path))

print(sum(len(follow_trail(trailhead, -1, grid)) for trailhead in trailheads))
