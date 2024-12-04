with open("./input.txt") as f:
    data = [list(l.strip()) for l in f]

part1 = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] != "X":
            continue
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            ci, cj = i, j
            for ch in "MAS":
                if ci + di >= len(data) or ci + di < 0 or cj + dj >= len(data[0]) or cj + dj < 0:
                    break
                if data[ci + di][cj + dj] != ch:
                    break
                ci += di
                cj += dj
            else:
                part1 += 1

print(part1)

part2 = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] != "A":
            continue
        s = ""
        for di, dj in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            if i + di >= len(data) or i + di < 0 or j + dj >= len(data[0]) or j + dj < 0:
                break
            s += data[i + di][j + dj]
        if s in ("MMSS", "SMMS", "SSMM", "MSSM"):
            part2 += 1

print(part2)
