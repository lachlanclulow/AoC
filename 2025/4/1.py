import pathlib


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    cells = {}
    rolls = []

    answer = 0

    for y, line in enumerate(puzzle_input.splitlines()):
        for x, cell in enumerate(line):
            if cell == "@":
                cells[(x, y)] = cell
                rolls.append((x, y))
    

    for roll in rolls:
        count = 0
        for x in range(roll[0]-1, roll[0]+2):
            for y in range(roll[1]-1, roll[1]+2):
                if (x, y) in cells:
                    count += 1
                if count > 4:
                    break
            if count > 4:
                break

        if count <= 4:
            answer += 1

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