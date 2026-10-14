gears: list[int | tuple[int,int]] = []

with open("part3.txt") as f:
    lines: list[str] = f.read().splitlines()
    gears.append(int(lines[0]))
    for line in lines[1:len(lines)-1]:
        num1, num2 = line.split("|")
        gears.append((int(num1), int(num2)))
    gears.append(int(lines[-1]))

curRotation: int = gears[0] / gears[1][0]

for idx, gearPair in enumerate(gears[2:-1]):
    curRotation *= gears[idx+1][1] / gearPair[0]

curRotation *= gears[-2][1] / gears[-1]

print(f"Final Gear Rotation = {int(curRotation * 100)}")

