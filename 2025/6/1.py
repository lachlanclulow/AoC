import pathlib


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0
    rows = puzzle_input.splitlines()
    operators = [x for x in rows[-1].split()]

    answers = [int(i) for i in rows[0].split()]
    for row in rows[1:-1]:
        for i, a in enumerate([int(j) for j in row.split()]):
            if operators[i] == "*":
                answers[i] *= a
            else:
                answers[i] += a


    return(sum(answers))


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