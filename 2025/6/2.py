import pathlib


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0
    rows = puzzle_input.splitlines()
    operators = [x for x in rows[-1].split()]

    answers = []
    i = 0
    nums = []
    for x in range(len(rows[0])):
        num = ""
        for y in range(len(rows)-1):
            if rows[y][x] != " ":
                num += rows[y][x]
        if num == "":
            if operators[i] == "*":
                answers.append(nums[0])
                for n in nums[1:]:
                    answers[-1] *= n
            else:
                answers.append(sum(nums))
            nums = []
            i+=1
        else:
            nums.append(int(num))
    
    if operators[i] == "*":
        answers.append(nums[0])
        for n in nums[1:]:
            answers[-1] *= n
    else:
        answers.append(sum(nums))
    
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