import re

example = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

example = open("3.puzz", "r").read()
total = 0
doreg = re.compile(r"do\(\)")
dontreg = re.compile(r"don't\(\)")
mulreg = re.compile(r"mul\((\d+),(\d+)\)")

line = "".join(example.splitlines())

do = True
for dont_split in re.split(dontreg, line):
    for do_split in re.split(doreg, dont_split):
        if do:
            for a, b in re.findall(mulreg, do_split):
                total += int(a)*int(b)
        do = True
    do = False

print(total)