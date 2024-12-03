import re

with open("./input.txt") as f:
    data = f.read()

part1, part2 = 0, 0
enabled = True
for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", data):
    if m.group(0).startswith("don't"):
        enabled = False
    elif m.group(0).startswith("do"):
        enabled = True
    else:
        a, b = m.group(1, 2)
        part1 += int(a) * int(b)
        if enabled:
            part2 += int(a) * int(b)

print(part1)
print(part2)
