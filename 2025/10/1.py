import pathlib
import sys

sys.setrecursionlimit(10000)

def search(n, buttons, seen, target, depth=0):

    if n in seen and seen[n] <= depth:
        return seen
    else:
        seen[n] = depth

    for button in buttons:
        d = search(n ^ button, buttons, seen, target, depth+1)
        if type(d) is dict:
            seen |= d
    
    return seen


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0
    
    for row in puzzle_input.splitlines():
        things = row.split()
        lights = int(things[0][1:-1].replace(".", "0").replace("#", "1")[::-1], 2)
        joltages = things[-1][1:-1].split(",")
        buttons = []
        for wires in [[int(y) for y in x[1:-1].split(",")] for x in things[1:-1]]:
            n = 0
            for w in wires:
                n += 2**w
            
            buttons.append(n)

        seen = {}


        answer += search(0, buttons, {}, lights)[lights]
        

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