with open("./input.txt") as f:
    garden = [list(l.rstrip()) for l in f]

m, n = len(garden), len(garden[0])

visited = set()
regions = []


def find_region(pt, i, j, region):
    if (i, j) in visited:
        return
    if garden[i][j] != pt:
        return
    visited.add((i, j))
    region.append((i, j))
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ci, cj = i + di, j + dj
        if not 0 <= ci < m or not 0 <= cj < n or (ci, cj) in visited:
            continue
        find_region(pt, ci, cj, region)


for i in range(m):
    for j in range(n):
        region = []
        find_region(garden[i][j], i, j, region)
        if region:
            regions.append(region)

part1 = 0
for region in regions:
    area = len(region)
    perimeter = 0
    for i, j in region:
        adj_i = sum(1 for ci, cj in region if cj == j and abs(ci - i) == 1)
        adj_j = sum(1 for ci, cj in region if ci == i and abs(cj - j) == 1)
        perimeter += 4 - adj_i - adj_j
    part1 += area * perimeter

print(part1)

part2 = 0
for region in regions:
    area = len(region)

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        edges = []
        for i, j in region:
            ci, cj = i + di, j + dj
            if (ci, cj) not in region:
                if di:
                    edges.append((ci, cj))
                else:
                    edges.append((cj, ci))
        edges.sort()
        sides = 1
        for i in range(len(edges) - 1):
            if (
                (edges[i][0] == edges[i + 1][0] and edges[i][1] + 1 == edges[i + 1][1])
                or (edges[i][1] == edges[i + 1][1] and edges[i][0] + 1 == edges[i + 1][0])
            ):
                continue
            sides += 1
        part2 += area * sides

print(part2)
