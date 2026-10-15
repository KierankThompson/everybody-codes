with open("part1.txt") as f:
    line: list[str] = f.readline().strip()


mentorCount: int = 0
possiblePairs: int = 0

for ch in line:
    if ch == "A":
        mentorCount += 1
    elif ch == "a":
        possiblePairs += mentorCount

print(f"{possiblePairs=}")