import pathlib

def search(target, ranges):
    print(f"{target=} {ranges[len(ranges)//2]}")
    if len(ranges) == 1:
        print(f"{target=} {ranges[0]} {ranges[0][0] <= target <= ranges[0][1]}")
        return ranges[0][0] <= target <= ranges[0][1]
    if target < ranges[len(ranges)//2][0]:
        return search(target, ranges[:len(ranges)//2])
    if target >= ranges[len(ranges)//2][0]:
        return search(target, ranges[len(ranges)//2:])
    return False


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0

    parts = puzzle_input.split("\n\n")

    fresh_ranges = sorted([tuple([int(y) for y in x.split("-")]) for x in parts[0].splitlines()], key=lambda x: x[0])
    ingredients = sorted([int(x) for x in parts[1].splitlines()])

    compressed_ranges = [fresh_ranges[0]]
    #print(fresh_ranges)

    for start, end in fresh_ranges[1:]:
        if start <= compressed_ranges[-1][1]:
            compressed_ranges[-1] = (compressed_ranges[-1][0], max(end, compressed_ranges[-1][1]))
        else:
            compressed_ranges.append((start, end))
    
    #print(compressed_ranges)

    for start, end in compressed_ranges:
        answer += end-start+1

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