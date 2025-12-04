import pathlib

def reduce(nums, l=11):
    if l<0:
        return ""
    if len(nums)-l == 1:
        return nums
    
    biggest = nums[0]
    pos = 0
    for i in range(len(nums)-l):
        if nums[i] > biggest:
            biggest = nums[i]
            pos = i

    return biggest + reduce(nums[pos+1:], l-1)



def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0

    for line in puzzle_input.splitlines():
        answer += int(reduce(line))
    return(answer)


if __name__ == "__main__":
    # print(main(
    #     open(
    #         pathlib.Path(__file__).parent.resolve().joinpath("example.txt"),
    #         "r"
    #     ).read()
    # ))
    print(main(
        open(
            pathlib.Path(__file__).parent.resolve().joinpath("input.txt"),
            "r"
        ).read()
    ))