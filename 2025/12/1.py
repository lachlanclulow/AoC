import pathlib


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0

    stuff = puzzle_input.split("\n\n")

    shape_sizes  = {}
    for shape_in in stuff[:-1]:
        rows = shape_in.splitlines()
        shape_sizes[int(rows[0].split(":")[0])] = 0
        for r in rows[1:]:
            ar = [1 if c == "#" else 0 for c in r]
            shape_sizes[int(rows[0].split(":")[0])] += sum(ar)

    for tree in stuff[-1].splitlines():
        dims, req = tuple(tree.split(": "))
        x, y = tuple([int(x) for x in dims.split("x")])
        reqs = []
        for i, d in enumerate(req.split()):
            reqs += [i] * int(d)  

        answer += sum([shape_sizes[x] for x in reqs]) < x*y

    return answer


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