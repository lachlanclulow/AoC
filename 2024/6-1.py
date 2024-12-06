example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

example = open("6.puzz", "r").read()

obstacles = set()
visited = set()
visited_with_dir = set()
height = len(example.splitlines())
width = len(example.splitlines()[0])
pos = None

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

dirs = {
    UP: (0, -1),
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0)
}

for y, line in enumerate(example.splitlines()):
    for x, cell in enumerate(line):
        if cell == "#":
            obstacles |= {(x, y)}
        elif cell == "^":
            pos = ((x, y), UP)
            visited |= {pos[0]}
            visited_with_dir |= {pos}

while True:
    next_pos = tuple(x+y for x, y in zip(pos[0], dirs[pos[1]]))
    if (next_pos, pos[1]) in visited_with_dir or next_pos[0] < 0 or next_pos[0] >= width or next_pos[1] < 0 or next_pos[1] >= height:
        print(len(visited))
        break
    if next_pos not in obstacles:
        pos = (next_pos, pos[1])
        visited_with_dir |= {pos}
        visited |= {pos[0]}
    else:
        pos = (pos[0], (pos[1] + 1) % 4)
