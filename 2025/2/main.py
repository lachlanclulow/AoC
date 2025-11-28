import pathlib


def main():
    puzzle_input = open(
        pathlib.Path(__file__).parent.resolve().joinpath("input.txt"),
        "r"
    ).read()

    # I'd like to solve the puzzle
    answer = 10

    return(answer)


if __name__ == "__main__":
    print(main())