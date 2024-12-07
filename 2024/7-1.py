example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

example = open("7.puzz", "r").read()

equations = []

def evaluate(target: int, numbers: list[int]):
    for state in range(2 ** (len(numbers) - 1)):
        total = numbers[0]

        curr_state = state
        for i in range(1, len(numbers)):
            if curr_state & 1:
                total *= numbers[i]
            else:
                total += numbers[i]
            curr_state >>= 1

        if total == target:
            return target
    return 0

t = 0

for line in example.splitlines():
    parts = line.split(": ")
    t += evaluate(int(parts[0]), [int(x) for x in parts[1].split(" ")])

print(t)

