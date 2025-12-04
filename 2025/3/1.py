import pathlib


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0

    for line in puzzle_input.splitlines():
        first = line[0]
        second = line[1]
        for i, c in enumerate(line[1:], 1):
            if c > first and i <= len(line)-2:
                first = c
                second = line[i+1]
            elif c > second:
                second = c        
        answer += int(first + second)

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