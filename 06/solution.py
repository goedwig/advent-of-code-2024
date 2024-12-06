from itertools import cycle

with open("./input.txt") as f:
    area = [list(l.rstrip()) for l in f]

m, n = len(area), len(area[0])
i0, j0 = next((i, row.index("^")) for i, row in enumerate(area) if "^" in row)


def part1():
    i, j = i0, j0
    dirs = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    di, dj = next(dirs)
    seen = {(i, j)}
    while True:
        ci = i + di
        cj = j + dj
        if not 0 <= ci < m or not 0 <= cj < n:
            break
        if area[ci][cj] == "#":
            di, dj = next(dirs)
            continue
        i, j = ci, cj
        area[i][j] = "X"
        seen.add((i, j))
    print(len(seen))


def part2():
    count = 0
    for row in range(m):
        for col in range(n):
            if (row, col) == (i0, j0):
                continue

            i, j = i0, j0
            dirs = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
            di, dj = next(dirs)
            seen = {(i, j, di, dj)}

            carea = [list(l) for l in area]
            carea[row][col] = "#"
            loop = False

            while True:
                ci = i + di
                cj = j + dj
                if not 0 <= ci < m or not 0 <= cj < n:
                    break
                if carea[ci][cj] == "#":
                    di, dj = next(dirs)
                    continue
                i, j = ci, cj
                if (i, j, di, dj) in seen:
                    loop = True
                    break
                seen.add((i, j, di, dj))

            if loop:
                count += 1

    print(count)


part1()
part2()
