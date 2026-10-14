with open("part1.txt") as f:
    input: str = f.readline().strip()

crateSizes: set[int] = set(map(int, input.split(",")))
print(f"Largest Set of Crates={sum(crateSizes)}")