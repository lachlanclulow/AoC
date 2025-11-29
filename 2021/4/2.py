import pathlib


def print_board(board):
    for r in range(5):
        for c in range(5):
            for n, cell in board["cells"].items():
                if cell == (r, c):
                    p = f"*{n}" if cell in board["marked"] else str(n)
                    print(p.rjust(4), end="")
        print()

def get_board(board_str: list[str]):
    board = {
        "rows": [0, 0, 0, 0, 0],
        "columns": [0, 0, 0, 0, 0],
        "cells": {},
        "marked": set(),
        "won": False
    }
    for i, row in enumerate(board_str):
        for j, cell in enumerate([int(x) for x in row.split()]):

            board["cells"][cell] = (i, j)


    return board

def main(puzzle_input: str):
    puzz_in = puzzle_input.splitlines()
    # I'd like to solve the puzzle
    numbers = [int(x) for x in puzz_in[0].split(",")]

    boards = []

    for i in range(2, len(puzz_in) - 2, 6):
        boards.append(get_board(puzz_in[i:i+5]))

    boards_left = len(boards)
    
    for number in numbers:
        for i, board in enumerate(boards):
            if not board["won"] and number in board["cells"]:
                board["rows"][board["cells"][number][0]] += 1
                board["columns"][board["cells"][number][1]] += 1
                board["marked"].add(board["cells"][number])

                if board["rows"][board["cells"][number][0]] == 5 or board["columns"][board["cells"][number][1]] == 5:
                    boards_left -= 1
                    board["won"] = True
                    answer = 0
                    for k, v in board["cells"].items():
                        if v not in board["marked"]:
                            answer += k
                    if boards_left == 0:
                        return answer * number


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