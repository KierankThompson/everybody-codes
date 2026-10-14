with open("part1.txt") as f:
    input: str = f.readline().strip()
    num1, num2 = map(int, input[3:-1].split(","))
    A: list[int] = [num1, num2]

R: list[int] = A

for i in range(2):
    R = [R[0] ** 2 - R[1] ** 2, R[1] * R[0] * 2]
    R = [R[0] // 10, R[1] // 10]
    R = [R[0] + A[0], R[1] + A[1]]

print(f"R=[{R[0]},{R[1]}]")