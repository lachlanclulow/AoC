import itertools

example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

example = open("8.puzz", "r").read()

antennae = {}
antinodes = set()

for y, line in enumerate(example.splitlines()):
    for x, cell in enumerate(line):
        if cell != '.':
            if cell in antennae:
                antennae[cell].append((x, y))
            else:
                antennae[cell] = [(x, y)]


for k, v in antennae.items():
    for a1, a2 in itertools.combinations(v, 2):
        dist = (a1[0]-a2[0], a1[1]-a2[1])
        antinodes.add((a1[0]+dist[0], a1[1]+dist[1]))
        antinodes.add((a2[0]-dist[0], a2[1]-dist[1]))
    
print(len([0 for _x,_y in antinodes if _x>=0 and _y>=0 and _x<=x and _y<=y]))