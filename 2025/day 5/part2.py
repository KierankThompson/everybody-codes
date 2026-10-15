from dataclasses import dataclass
from typing import Optional

with open("part2.txt") as f:
    lines: list[str] = f.read().splitlines()
    swords: list[list[int]] = [list(map(int, line.split(":")[1].split(","))) for line in lines]



@dataclass
class SpineSeg():
    value: int
    leftValue: Optional[int] = None
    rightValue: Optional[int] = None

swordQualities: list[int] = []
for sword in swords:
    fishbone = []
    for num in sword:
        inserted: bool = False
        for seg in fishbone:
            if num < seg.value and not seg.leftValue:
                seg.leftValue = num
                inserted = True
                break
            if num > seg.value and not seg.rightValue:
                seg.rightValue = num
                inserted = True
                break
        if not inserted:
            fishbone.append(SpineSeg(num))

    swordQualities.append(int("".join([str(seg.value) for seg in fishbone])))

print(f"Quality Difference is {max(swordQualities) - min(swordQualities)}")



