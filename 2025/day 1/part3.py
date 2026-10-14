with open("part3.txt") as f:
    lines: list[str] = f.readlines()
    names: list[str] = lines[0].strip().split(",")
    directions: list[str] = lines[2].strip().split(",")


numNames: int = len(names)
for direc in directions:
    amount: int = int(direc[1:])
    if direc[0] == "R":
        swapIndex: int = 0 + amount
    else:
        swapIndex = 0 - amount

    swapIndex %= numNames

    names[0], names[swapIndex] = names[swapIndex], names[0]

print(f"Name is {names[0]}")
