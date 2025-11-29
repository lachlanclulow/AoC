import pathlib


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0

    report = puzzle_input.splitlines()

    results = [0 for _ in report[0]]

    for row in report:
        for i, bit in enumerate(row):
            results[i] += int(bit)
    
    gamma = 0
    epsilon = 0

    for result in results:
        gamma *= 2
        epsilon *= 2
        if result > len(report)/2:
            gamma += 1
        else:
            epsilon += 1

    return(gamma * epsilon)


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