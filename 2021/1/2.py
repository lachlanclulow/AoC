import pathlib


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0
    readings = puzzle_input.splitlines()
    last_reading = int(readings[0])
    for reading in readings[1:]:
        if int(reading) > last_reading:
            answer += 1
        last_reading = int(reading)

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