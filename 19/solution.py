from functools import cache

with open("./input.txt") as f:
    towels, patterns = f.read().split("\n\n")

towels = sorted(towels.split(", "), key=len, reverse=True)
patterns = patterns.split()


@cache
def decompose_pattern(pattern):
    if not len(pattern):
        return 1

    matched = []
    for towel in towels:
        if pattern.startswith(towel):
            matched.append(pattern.removeprefix(towel))

    if not matched:
        return 0

    return sum(decompose_pattern(pat) for pat in matched)


part1 = part2 = 0
for i, pattern in enumerate(patterns):
    nways = decompose_pattern(pattern)
    part1 += bool(nways)
    part2 += nways

print(part1)
print(part2)
