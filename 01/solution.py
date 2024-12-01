lcol, rcol = [], []

with open("./input.txt") as f:
    for l in f:
        a, b = l.split()
        lcol.append(int(a))
        rcol.append(int(b))

lcol.sort()
rcol.sort()

part1, part2 = 0, 0
for a, b in zip(lcol, rcol):
    part1 += abs(a - b)
    part2 += a * rcol.count(a)

print(part1)
print(part2)
