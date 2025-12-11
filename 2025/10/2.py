import pathlib
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def gauss_elim(buttons, joltages) -> int:
    mat = np.zeros((len(joltages), len(buttons)))
    for i, button in enumerate(buttons):
        for j in button:
            if j < len(joltages):
                mat[j, i] = 1
    
    soln = milp(
        np.ones(len(buttons)),
        constraints=LinearConstraint(
            mat,
            np.array(joltages),
            np.array(joltages)),
        bounds=Bounds(lb=0, ub=max(joltages)),
        integrality=np.ones(len(buttons))
    )
    
    return int(round(soln.fun))


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0
    
    for row in puzzle_input.splitlines():
        things = row.split()
        joltages = tuple([int(x) for x in things[-1][1:-1].split(",")])
        buttons = [tuple([int(y) for y in x[1:-1].split(",")]) for x in things[1:-1]]

        answer += gauss_elim(buttons, joltages)


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
