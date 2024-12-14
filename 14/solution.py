import re
from collections import Counter
from functools import reduce
from operator import mul


def nums(s):
    return tuple(int(n) for n in re.findall("-?\d+", s))


positions, velocities = [], []
with open("./input.txt") as f:
    for l in f:
        n = nums(l)
        positions.append(n[:2])
        velocities.append(n[2:])

w = 101
h = 103


# Part 1
def part1(positions):
    for _ in range(100):
        for i in range(len(positions)):
            (x, y), (dx, dy) = positions[i], velocities[i]
            positions[i] = (x + dx) % w, (y + dy) % h

    wm = w // 2
    hm = h // 2
    c = Counter()
    for x, y in positions:
        if x == wm or y == hm:
            continue
        xs = (x > wm) - (x < wm)
        ys = (y > hm) - (y < hm)
        c[(xs, ys)] += 1

    print(reduce(mul, c.values()))


def has_tree(positions):
    positions = set(positions)
    t = [
        (3, 0),
        (2, 1), (3, 1), (4, 1),
        (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
        (3, 4),
    ]
    tw = 8
    th = 5
    for dx in range(w - tw):
        for dy in range(h - th):
            ct = set((x + dx, y + dy) for x, y in t)
            if ct <= positions:
                return ct
    return None


# Part 2
def part2(positions):
    s = 1
    while True:
        for i in range(len(positions)):
            (x, y), (dx, dy) = positions[i], velocities[i]
            positions[i] = (x + dx) % w, (y + dy) % h
        if has_tree(positions):
            break
        s += 1
    print(s)


part1(positions[:])
part2(positions[:])
