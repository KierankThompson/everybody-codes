with open("part1.txt") as f:
    lines: list[str] = f.readlines()
    names: list[str] = lines[0].strip().split(",")
    directions: list[str] = lines[2].strip().split(",")

curIndex: int = 0
numNames: int = len(names)
for direc in directions:
    amount: int = int(direc[1:])
    if direc[0] == "R":
        curIndex = min(curIndex + amount, numNames-1)
    else:
        curIndex = max(curIndex - amount, 0)

print(f"Name is {names[curIndex]}")