import pathlib


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0
    f = 0
    d = 0
    for dir, mag in [x.split(" ") for x in puzzle_input.splitlines()]:
        if dir == "up":
            d -= int(mag)
        elif dir == "down":
            d += int(mag)
        else:
            f += int(mag)

    return(f*d)


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