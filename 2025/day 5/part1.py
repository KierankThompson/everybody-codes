from dataclasses import dataclass
from typing import Optional

with open("part1.txt") as f:
    line: list[str] = f.readline().strip()
    nums: list[int] = list(map(int, line.split(":")[1].split(",")))

@dataclass
class SpineSeg():
    value: int
    leftValue: Optional[int] = None
    rightValue: Optional[int] = None



fishbone = []
for num in nums:
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

print(f"Quality = {"".join([str(seg.value) for seg in fishbone])}")



