import pathlib


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0
    readings = puzzle_input.splitlines()

    for i, reading in enumerate(readings[:-3]):
        #print(f"{i=}: {reading} < {readings[i+3]}")
        if int(reading) < int(readings[i+3]):
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
