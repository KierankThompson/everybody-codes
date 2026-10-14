with open("part2.txt") as f:
    input: str = f.readline().strip()

crateSizes: set[int] = set(map(int, input.split(",")))
sortedCrateSizes: list[int] = sorted(list(crateSizes))
print(f"Largest Set of Crates={sum(sortedCrateSizes[:20])}")