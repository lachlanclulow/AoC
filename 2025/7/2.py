import pathlib


def beam(x, y, rows, explored={}):
    if y == len(rows):
        explored[(x, y)] = 1
        return explored, 1
    
    if (x, y) in explored:
        return explored, explored[(x, y)]
    
    if rows[y][x] == "^":
        left = beam(x-1, y, rows, explored)
        right = beam(x+1, y, rows, explored)

        explored |= left[0]
        explored |= right[0]
        explored[(x, y)] = left[1] + right[1]

        return explored, left[1]+right[1]
    return beam(x, y+1, rows, explored)
        
        

def main(puzzle_input: str):
    # I'd like to solve the puzzle
    rows = puzzle_input.splitlines()

    y = 1
    x = 0

    for i, c in enumerate(rows[0]):
        if c == "S":
            x = i
            break
    
    paths = beam(x, y, rows)

    return(paths[1])


if __name__ == "__main__":
    print(main(
        open(
            pathlib.Path(__file__).parent.resolve().joinpath("example.txt"),
            "r"
        ).read()
    ))
    print(main(
        open(
            pathlib.Path(__file__).parent.resolve().joinpath("input.txt"),
            "r"
        ).read()
    ))