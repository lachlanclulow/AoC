import pathlib
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0

    coords = []

    for row in puzzle_input.splitlines():
        x, y = tuple([int(x) for x in row.split(",")])

        coords.append((x, y))
    
    poly = Polygon(coords)


    for x1, y1 in coords:
        for x2, y2 in coords:
            if x1 != x2 and y1 != y2:
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                if area > answer and poly.contains(Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])):
                    answer = area

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