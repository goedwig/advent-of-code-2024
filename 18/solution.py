with open("./input.txt") as f:
    data = f.read().split("\n")

corrupted = set()
m = n = 71


def bfs():
    queue = [(0, 0, 0)]
    visited = {(0, 0)}
    while queue:
        x, y, steps = queue.pop(0)

        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy

            if (nx, ny) == (m - 1, n - 1):
                return steps + 1

            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in corrupted and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))


for i, l in enumerate(data):
    x, y = map(int, l.split(","))
    corrupted.add((x, y))

    if i == 1023:
        print(bfs())  # part 1
    elif i > 1023 and not bfs():
        print(f"{x},{y}")  # part 2
        break
