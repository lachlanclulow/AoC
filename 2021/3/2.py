import pathlib


def search(readings: list[str], i: int, reverse: bool=False) -> str:
    if len(readings) == 1:
        return readings[0]
    
    s_readings = sorted(readings,  key=lambda x: x[i], reverse=reverse)
    lower_bit = s_readings[0][i]
    for j, row in enumerate(s_readings):
        if row[i] != lower_bit:
            if not reverse:
                if j <= len(readings)/2:
                    return search(s_readings[j:], i+1, reverse)
                return search(s_readings[:j], i+1, reverse)
            else:
                if j >= len(readings)/2:
                    return search(s_readings[j:], i+1, reverse)
                return search(s_readings[:j], i+1, reverse)




def main(puzzle_input: str):
    # I'd like to solve the puzzle
    report = puzzle_input.splitlines()

    o2 = search(report, 0)
    co2 = search(report, 0, True)

    o2_i = 0
    for x in o2:
        o2_i *= 2
        if x == "1":
            o2_i += 1
    
    co2_i = 0
    for x in co2:
        co2_i *= 2
        if x == "1":
            co2_i += 1

    return o2_i * co2_i


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