from collections import defaultdict
with open("part1.txt") as f:
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

for name in names:
    seenCh: set[str] = {}
    validName: bool = True
    for idx, ch in enumerate(name[:-1]):
        if ch in ruleDict:
            if name[idx+1] not in ruleDict[ch]:
                validName = False
                break
    if validName:
        print(f"Name is {name}")
        break


