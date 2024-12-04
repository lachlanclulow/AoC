import sys

example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

# example = open("4.puzz", "r").read()

rows = example.splitlines()
total = 0

for i in range(len(rows)):
    for j in range(len(rows[i])):
        # Check left right
        if rows[i][j:].startswith("XMAS") or rows[i][j:].startswith("SAMX"):
            total += 1

        # Check up down
        if i <= len(rows) - 4:
            down = "".join([rows[i+k][j] for k in range(0, 4)])
            if down.startswith("XMAS") or down.startswith("SAMX"):
                total += 1

        # Check diagonal down-right
        if i <= len(rows) - 4 and j <= len(rows[i]) - 4:
            diag = "".join([rows[i+k][j+k] for k in range(0, 4)])
            if diag.startswith("XMAS") or diag.startswith("SAMX"):
                total += 1

        # Check diagonal down-left
        if i <= len(rows) - 4 and j >= 3:
            diag = "".join([rows[i+k][j-k] for k in range(0, 4)])
            if diag.startswith("XMAS") or diag.startswith("SAMX"):
                total += 1

print(total)