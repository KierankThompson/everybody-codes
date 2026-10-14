with open("part2.txt") as f:
    lines: list[str] = f.readlines()
    names: list[str] = lines[0].strip().split(",")
    directions: list[str] = lines[2].strip().split(",")

curIndex: int = 0
numNames: int = len(names)
for direc in directions:
    amount: int = int(direc[1:])
    if direc[0] == "R":
        curIndex = curIndex + amount
    else:
        curIndex = curIndex - amount

    curIndex %= numNames

print(f"Name is {names[curIndex]}")
