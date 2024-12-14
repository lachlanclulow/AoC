example = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

example = open("13.puzz", "r").read()

games = example.split("\n\n")

total = 0

for game in games:
    rows = game.splitlines()

    a_x = int(rows[0].split(',')[0].split("+")[1])
    a_y = int(rows[0].split(',')[1].split("+")[1])
    b_x = int(rows[1].split(',')[0].split("+")[1])
    b_y = int(rows[1].split(',')[1].split("+")[1])
    p_x = int(rows[2].split(',')[0].split("=")[1])
    p_y = int(rows[2].split(',')[1].split("=")[1])

    d = (a_x * b_y - a_y * b_x)

    a = (p_x * b_y - p_y * b_x)
    b = (p_y * a_x - p_x * a_y)

    if a % d == 0 and b % d == 0:
        total += 3*a//d + b//d

print(total)

    