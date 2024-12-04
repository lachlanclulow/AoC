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
        if rows[i][j] == "A" and i > 0 and j > 0 and i < len(rows) - 1 and j < len(rows[i]) - 1:
            diag_1 = "".join([rows[i-1+k][j-1+k] for k in range(0, 3)])
            diag_2 = "".join([rows[i+1-k][j-1+k] for k in range(0, 3)])
            if (diag_1.startswith("MAS") or diag_1.startswith("SAM")) and (diag_2.startswith("MAS") or diag_2.startswith("SAM")):
                total += 1
        
print(total)