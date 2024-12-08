from string import digits, ascii_letters

antinodes = digits + ascii_letters

with open("./input.txt") as f:
    data = [list(l.rstrip()) for l in f]

m = len(data)
n = len(data[0])


def get_antinodes(i1, j1, i2, j2, p2=False):
    seen = set()

    di = i2 - i1
    dj = j2 - j1

    for i, j, cdi, cdj in [(i1, j1, -di, -dj), (i2, j2, di, dj)]:
        ai = i + cdi
        aj = j + cdj
        while 0 <= ai < m and 0 <= aj < n:
            seen.add((ai, aj))
            if not p2:
                break
            ai = ai + cdi
            aj = aj + cdj

    return seen


def solve(p2=False):
    seen = set()
    for i1 in range(m):
        for j1 in range(n):
            a = data[i1][j1]
            if a not in antinodes:
                continue
            for i2 in range(i1, m):
                if i2 == i1:
                    r = range(j1 + 1, n)
                else:
                    r = range(n)

                for j2 in r:
                    if data[i2][j2] != a:
                        continue

                    if p2:
                        seen |= {(i1, j1), (i2, j2)}
                    seen |= get_antinodes(i1, j1, i2, j2, p2)
    print(len(seen))


solve()
solve(p2=True)
