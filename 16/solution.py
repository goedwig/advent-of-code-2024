import heapq
from functools import reduce

with open("./input.txt") as f:
    maze = f.read().split("\n")

m, n = len(maze), len(maze[0])
si, sj = m - 2, 1
ei, ej = 1, n - 2


def find_shortest_paths():
    pq = []
    heapq.heappush(pq, (0, si, sj, 0, 1, [(si, sj)]))
    scores = {(si, sj, 0, 1): 0}
    paths = {}

    while pq:
        score, i, j, di, dj, path = heapq.heappop(pq)

        if i == ei and j == ej:
            paths.setdefault(score, []).append(path + [(ei, ej)])
            continue

        next_moves = [(di, dj)]

        if (di, dj) in [(0, 1), (0, -1)]:  # >, <
            next_moves += [(-1, 0), (1, 0)]  # ^, v
        elif (di, dj) in [(-1, 0), (1, 0)]:  # ^, v
            next_moves += [(0, 1), (0, -1)]  # >, <

        for cdi, cdj in next_moves:
            ci, cj = i + cdi, j + cdj
            cscore = score + (1 if (di, dj) == (cdi, cdj) else 1001)

            if (
                0 < ci < m - 1
                and 0 < cj < n - 1
                and maze[ci][cj] != "#"
                and cscore <= scores.get((ci, cj, cdi, cdj), float("inf"))
            ):
                scores[ci, cj, cdi, cdj] = cscore
                path = path[:]
                path.append((i, j))
                heapq.heappush(pq, (cscore, ci, cj, cdi, cdj, path))

    min_score = min(paths)
    return min_score, paths[min_score]


score, paths = find_shortest_paths()

print(score)  # part 1

tiles = reduce(set.union, paths, set())

print(len(tiles))  # part 2
