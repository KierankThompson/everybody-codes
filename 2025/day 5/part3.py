from dataclasses import dataclass
from typing import Optional

with open("part3.txt") as f:
    lines: list[str] = f.read().splitlines()
    swords: list[list[int]] = [list(map(int, line.split(":")[1].split(","))) for line in lines]
    ids: list[int] = [int(line.split(":")[0]) for line in lines]



@dataclass
class SpineSeg():
    value: int
    leftValue: Optional[int] = None
    rightValue: Optional[int] = None

@dataclass
class SwordData():
    fishbone: list[SpineSeg]
    id: int 
    quality: int
    def __lt__(self, other: SwordData) -> bool:
        if self.quality < other.quality:
            return True
        if self.quality > other.quality:
            return False

        def levelStr(level: SpineSeg) -> str:
            levelStr = ""
            if level.leftValue:
                levelStr += str(level.leftValue)
            levelStr += str(level.value)
            if level.rightValue:
                levelStr += str(level.rightValue)
            return levelStr
        
        for s, o in zip(self.fishbone, other.fishbone):
            sStr: str = levelStr(s)
            oStr: str = levelStr(o)

            if int(sStr) < int(oStr):
                return True
            if int(sStr) > int(oStr):
                return False
            
        return self.id < other.id
            
    def __repr__(self):
        return f"{self.id} {self.quality}"
            
swordDataArr: list[SwordData] = []
for sword, curId in zip(swords, ids):
    fishbone: list[SpineSeg] = []
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
    
    curQuality = int("".join([str(seg.value) for seg in fishbone]))
    swordDataArr.append(SwordData(fishbone, curId, curQuality))


swordDataArr.sort(reverse=True)

ans: int = 0
for idx, swordD in enumerate(swordDataArr):
    ans += swordD.id * (idx+1)

print(f"{ans=}")






