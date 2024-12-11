example = """125 17"""

example = open("11.puzz", "r").read()

def blink_stone(stone, blinks=0) -> int:
    if blinks == 25:
        return 1
    if stone == 0:
        return blink_stone(1, blinks + 1)
    if len(str(stone)) % 2 == 0:
        return blink_stone(int(str(stone)[:len(str(stone))//2]), blinks + 1) + \
            blink_stone(int(str(stone)[len(str(stone))//2:]), blinks + 1)
    else:
        return blink_stone(stone * 2024, blinks + 1)

print(sum([blink_stone(int(s)) for s in example.split(" ")]))
