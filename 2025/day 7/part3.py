from collections import defaultdict, deque

with open("part3.txt") as f:
    lines: list[str] = f.read().splitlines()
    names: list[str] = lines[0].split(",")
    rules: list[str] = lines[2:]

    ruleDict: defaultdict[str, list[str]] = defaultdict(list)
    for rule in rules:
        preceedCh, succeedStr = rule.split(">")
        preceedCh = preceedCh.strip()
        succeedChs: list[str] = succeedStr.strip().split(",")

        for ch in succeedChs:
            ruleDict[preceedCh].append(ch)

ans: int = 0
possibleNames: set[str] = set()
for i, name in enumerate(names):
    seenCh: set[str] = {}
    validName: bool = True
    for idx, ch in enumerate(name[:-1]):
        if ch in ruleDict:
            if name[idx+1] not in ruleDict[ch]:
                validName = False
                break
    if validName:
        queue: deque[str] = deque([name])
        
        while queue:
            curName: str = queue.popleft()
            if curName in possibleNames:
                continue

            if 7 <= len(curName) <= 11:
                possibleNames.add(curName)

            if curName[-1] in ruleDict and len(curName) < 11:
                for ch in ruleDict[curName[-1]]:
                    queue.append(curName + ch)

    

print(f"Number of possible names is {len(possibleNames)}")



