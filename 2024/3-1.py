import re

example = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

example = open("3.puzz", "r").read()
total = 0
for line in example.splitlines():
    reg = re.compile(r"mul\((\d+),(\d+)\)")

    for a, b in re.findall(reg, line):
        total += int(a)*int(b)

print(total)