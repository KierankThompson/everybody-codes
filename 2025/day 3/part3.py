from collections import Counter
with open("part3.txt") as f:
    input: str = f.readline().strip()

crateSizes = list(map(int, input.split(",")))
crateSizeCount: Counter[int, int] = Counter(crateSizes)
print(f"Number of sets= {max(crateSizeCount.values())}")