import pathlib


def beam(x, y, rows, path=set(), splits=set()):
    if y == len(rows):
        return path, splits
    if rows[y][x] == "^":
        left_p = path
        right_p = path
        left_s = splits
        right_s = splits

        if (x-1, y) not in path:
            left_p, left_s = beam(x-1, y, rows, path | {(x-1, y)}, splits | {(x, y)})
        if (x+1, y) not in path:
            right_p, right_s = beam(x+1, y, rows, left_p | {(x+1, y)}, left_s | {(x, y)})
        return left_p | right_p, left_s | right_s
    else:
        path.add((x, y))
        return beam(x, y+1, rows, path, splits)

def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0
    rows = puzzle_input.splitlines()

    y = 1
    x = 0

    for i, c in enumerate(rows[0]):
        if c == "S":
            x = i
            break
    
    path, splits = beam(x, y, rows)

    for y in range(len(rows)):
        for x in range(len(rows[0])):
            if (x, y) in path:
                print("|", end="")
            else:
                print(rows[y][x], end="")
        print()

    print(len(splits))




    return(answer)


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