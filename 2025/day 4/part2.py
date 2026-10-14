import math

with open("part2.txt") as f:
    lines: list[str] = f.read().splitlines()
    gears: list[int] = [int(line) for line in lines]

curRotation: int = 1

for idx, gear in enumerate(gears[1:]):
    curRotation *= (gears[idx] / gear) 

print(f"Turns Needed for 10000000000000 rotations = {math.ceil(10000000000000 / curRotation)}")