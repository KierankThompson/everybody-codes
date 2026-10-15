from collections import defaultdict
with open("part2.txt") as f:
    line: list[str] = f.readline().strip()


mentorsCount: defaultdict[str, int] = defaultdict(int)
possiblePairs: int = 0

for ch in line:
    if ch.isupper():
        mentorsCount[ch.lower()] += 1
    else:
        possiblePairs += mentorsCount[ch]

print(f"{possiblePairs=}")