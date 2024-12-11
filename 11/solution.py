from collections import Counter

with open("./input.txt") as f:
    stones = list(map(int, f.read().split()))


def blink(iterations):
    global stones

    c = Counter({stone: 1 for stone in stones})
    for _ in range(iterations):
        nc = Counter()
        for stone, count in c.items():
            if stone == 0:
                nc[1] += count
            elif len((stone_str := str(stone))) % 2 == 0:
                m = len(stone_str) // 2
                nc[int(stone_str[:m])] += count
                nc[int(stone_str[m:])] += count
            else:
                nc[stone * 2024] += count
        c = nc

    print(c.total())


blink(25)
blink(75)
