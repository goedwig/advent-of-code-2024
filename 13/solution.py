import re

with open("./input.txt") as f:
    data = f.readlines()


def nums(s):
    return tuple(int(n) for n in re.findall("\d+", s))


def cmm(i, prize_delta=0):
    machine = data[i:i + 3]
    a1, a2 = nums(machine[0])
    b1, b2 = nums(machine[1])
    prize_x, prize_y = nums(machine[2])
    c1 = -(prize_x + prize_delta)
    c2 = -(prize_y + prize_delta)

    x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
    y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)

    if x.is_integer() and y.is_integer():
        return int(x * 3 + y)
    else:
        return 0


part1, part2 = 0, 0
for i in range(0, len(data), 4):
    part1 += cmm(i)
    part2 += cmm(i, 10000000000000)

print(part1)
print(part2)
