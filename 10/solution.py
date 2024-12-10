with open("./input.txt") as f:
    tm = [list(map(int, l.rstrip())) for l in f]

m, n = len(tm), len(tm[0])


def hike(i, j, seen, p2=False):
    if not p2:
        seen.add((i, j))
    if tm[i][j] == 9:
        return 1
    trails = 0
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ci, cj = i + di, j + dj
        if not 0 <= ci < m or not 0 <= cj < n or (ci, cj) in seen or tm[ci][cj] - tm[i][j] != 1:
            continue
        trails += hike(ci, cj, seen, p2)
    return trails


part1, part2 = 0, 0
for i in range(m):
    for j in range(n):
        if tm[i][j] == 0:
            part1 += hike(i, j, set())
            part2 += hike(i, j, set(), p2=True)

print(part1)
print(part2)
