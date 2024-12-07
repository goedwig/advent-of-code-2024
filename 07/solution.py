with open("./input.txt") as f:
    data = f.readlines()


def calc(val, eq, cval, nval_i, p2=False):
    if nval_i >= len(eq):
        return val == cval
    conds = [
        calc(val, eq, cval + eq[nval_i], nval_i + 1, p2=p2),
        calc(val, eq, cval * eq[nval_i], nval_i + 1, p2=p2),
        calc(val, eq, int(f"{cval}{eq[nval_i]}"), nval_i + 1, p2=p2) if p2 else False
    ]
    return any(conds)


part1, part2 = 0, 0
for l in data:
    left, right = l.rstrip().split(":")
    val = int(left)
    eq = list(map(int, right.split()))
    if calc(val, eq, eq[0], 1):
        part1 += val
    if calc(val, eq, eq[0], 1, p2=True):
        part2 += val

print(part1)
print(part2)
