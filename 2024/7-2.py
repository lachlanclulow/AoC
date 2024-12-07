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

def add_trinary(val: list):
    carry = True

    for i in reversed(range(len(val))):
        if not carry:
            return val
        if val[i] + 1 > 2:
            val[i] = 0
        else:
            carry = False
            val[i] += 1
    if carry:
        val = [1] + val
    return val
            

def evaluate(target: int, numbers: list[int]):
    state = [0] * (len(numbers) - 1)
    final_state = [1] + [0] * (len(numbers) - 1)
    while state != final_state:
        total = numbers[0]

        for i in range(len(state)):
            if state[i] == 0:
                total += numbers[i+1]
            elif state[i] == 1:
                total *= numbers[i+1]
            elif state[i] == 2:
                total = int(str(total) + str(numbers[i+1]))

        state = add_trinary(state)
        if total == target:
            return target
    return 0

t = 0

for line in example.splitlines():
    parts = line.split(": ")
    t += evaluate(int(parts[0]), [int(x) for x in parts[1].split(" ")])

print(t)
