with open("part3.txt") as f:
    input: str = f.readline().strip()
    x: int
    y: int
    x, y = map(int, input[3:-1].split(","))
    


count: int = 0
for num1 in range(0, 1001, 1):
    for num2 in range(0, 1001, 1):
        A: list[int] = [x + num1, y + num2]

        R: list[int] = A
        exceeded: bool = False
        for _ in range(99):
            R = [R[0] ** 2 - R[1] ** 2, R[1] * R[0] * 2]
            R = [int(R[0] / 100000), int(R[1] / 100000)]
            R = [R[0] + A[0], R[1] + A[1]]

            if abs(R[0]) > 1000000 or abs(R[1]) > 1000000:
                exceeded = True
                break

        if not exceeded:
            count += 1

print(f"{count=}")