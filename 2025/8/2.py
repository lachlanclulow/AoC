import pathlib
import math
import heapq

def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)

def main(puzzle_input: str):
    # I'd like to solve the puzzle
    answer = 0
    circuits = {}
    for row in puzzle_input.split():
        x, y, z = tuple([int(x) for x in row.split(",")])
        circuits[(x, y, z)] = {(x, y, z)}
    
    distances = []

    compared = set()

    for k1 in circuits.keys():
        for k2 in circuits.keys():
            if k1 != k2 and (k1, k2) not in compared:
                heapq.heappush(distances, (distance(k1, k2), k1, k2))
                compared.add((k1, k2))
                compared.add((k2, k1))

    while len(distances) > 0:
        d, n1, n2 = heapq.heappop(distances)
        if n2 not in circuits[n1]:
            new_circuit = circuits[n1] | circuits[n2]
            for c in circuits[n1] | circuits[n2]:
                new_circuit |= circuits[c]
            if len(new_circuit) == len(circuits):
                return n1[0] * n2[0]
            circuits[n1] = new_circuit
            circuits[n2] = new_circuit
            for c in new_circuit:
                circuits[c] = new_circuit



if __name__ == "__main__":
    # print(main(
    #     open(
    #         pathlib.Path(__file__).parent.resolve().joinpath("example.txt"),
    #         "r"
    #     ).read()
    # ))
    print(main(
        open(
            pathlib.Path(__file__).parent.resolve().joinpath("input.txt"),
            "r"
        ).read()
    ))