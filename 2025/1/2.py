import pathlib


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 50
    count = 0

    for line in puzzle_input.splitlines():
        rots = 0
        if line[0] == "R":
            rots = (answer + int(line[1:])) // 100
            answer = (answer + int(line[1:])) % 100
        else:
            rots = abs((answer - int(line[1:])) // 100)
            if answer == 0:
                rots -= 1
            answer = (answer - int(line[1:])) % 100
            if answer == 0:
                rots += 1
        count += rots


    return count


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