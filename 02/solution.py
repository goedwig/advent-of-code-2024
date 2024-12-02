with open("./input.txt") as f:
    reports = [list(map(int, l.split())) for l in f]


def check_report(r, tolerate=False):
    safe = True
    sign = 0
    for i in range(len(r) - 1):
        d = r[i] - r[i + 1]
        if abs(d) not in range(1, 4):
            safe = False
        d_sign = (d > 0) - (d < 0)
        if not sign:
            sign = d_sign
        elif sign != d_sign:
            safe = False

        if not safe:
            if tolerate:
                r1, r2 = r[:], r[:]
                r1.pop(i)
                r2.pop(i + 1)
                safe = check_report(r1) or check_report(r2)
                if not safe and i == 1:
                    safe = check_report(r[1:])
                return safe
            else:
                break

    return safe


part1, part2 = 0, 0
for r in reports:
    part1 += check_report(r)
    part2 += check_report(r, tolerate=True)

print(part1)
print(part2)
