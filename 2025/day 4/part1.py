with open("part1.txt") as f:
    lines: list[str] = f.read().splitlines()
    gears: list[int] = [int(line) for line in lines]

curRotation: int = 1

for idx, gear in enumerate(gears[1:]):
    curRotation *= (gears[idx] / gear) 

print(f"Final Gear Rotation = {int(curRotation * 2025)}")