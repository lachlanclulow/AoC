import pathlib

def search(node, nodes, path, paths, target):
    if node == target:
        return 1
    if node in paths:
        return paths[node]
    if node in path:
        return 0
    if node not in nodes:
        return 0

    res = sum([search(n, nodes, {node} | path, paths, target) for n in nodes[node]])
    paths[node] = res
    return res
    


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0

    nodes = {}

    for row in puzzle_input.splitlines():
        node, paths = tuple(row.split(": "))
        nodes[node] = paths.split()
    
    answer = (
        search("svr", nodes, set(), {}, "fft")
        * search("fft", nodes, set(), {}, "dac")
        * search("dac", nodes, set(), {}, "out")
    ) + (
        search("svr", nodes, set(), {}, "dac")
        * search("dac", nodes, set(), {}, "fft")
        * search("fft", nodes, set(), {}, "out")
    )

    return(answer)


if __name__ == "__main__":
    print(main(
        open(
            pathlib.Path(__file__).parent.resolve().joinpath("example2.txt"),
            "r"
        ).read()
    ))
    print(main(
        open(
            pathlib.Path(__file__).parent.resolve().joinpath("input.txt"),
            "r"
        ).read()
    ))