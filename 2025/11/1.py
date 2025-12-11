import pathlib

def search(node, nodes, seen, target):
    if node == target:
        return 1

    return sum([search(n, nodes, seen, target) for n in nodes[node]])

def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0

    nodes = {}

    for row in puzzle_input.splitlines():
        node, paths = tuple(row.split(": "))
        nodes[node] = paths.split()
    
    answer = search("you", nodes, set(), "out")
        

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