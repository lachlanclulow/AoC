import pathlib


def main(puzzle_input: str):
    id_ranges = [(x.split('-')[0], x.split('-')[1]) for x in puzzle_input.split(',')]
    # I'd like to solve the puzzle
    answer = 0

    for start, end in id_ranges:
        for x in range(int(start), int(end) + 1):
            s_x = str(x)
            l = len(s_x)

            for i in range(2, l+1):
                invalid = True
                if l % i != 0:
                    continue
            
                chunk1 = s_x[:l//i]
            
                for chunk in range(1, i):
                    if s_x[chunk*l//i:(chunk+1)*l//i] != chunk1:
                        invalid = False
                        break

                if invalid:
                    answer += x
                    break
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