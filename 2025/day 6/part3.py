from collections import defaultdict
import math

with open("part3.txt") as f:
    line: list[str] = f.readline().strip()

lineLen: int = len(line)
mentorsCount: defaultdict[str, list[int]] = defaultdict(list)
possiblePairs: int = 0

for idx, ch in enumerate(line):
    if ch.isupper():
        mentorsCount[ch.lower()].append(idx)
    

for idx, ch in enumerate(line):
    if ch.islower():
        for mentorPos in mentorsCount[ch]:
            offset: int = mentorPos - idx
            
            kMin: int = math.ceil((-1000 - offset) / lineLen)
            kMax: int = math.floor((1000 - offset) / lineLen)
            
            for k in range(kMin, kMax + 1):
                validBlocks = 1000 - abs(k)
                
                if validBlocks > 0:
                    possiblePairs += validBlocks

print(f"{possiblePairs=}")