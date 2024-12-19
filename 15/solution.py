with open("./input.txt") as f:
    data = f.read()

wmap_raw, moves = data.split("\n\n")


def move_x(wmap, i, j, dj):
    if wmap[i][j] == "#":
        return False

    if wmap[i][j] == ".":
        return True

    cj = j + dj

    if move_x(wmap, i, cj, dj):
        wmap[i][cj] = wmap[i][j]
        wmap[i][j] = "."
        return True

    return False


def move_y(wmap, i, j, di, checkonly=True):
    if wmap[i][j] == "#":
        return False

    if wmap[i][j] == ".":
        return True

    ci = i + di

    if wmap[i][j] in ("@", "O") and move_y(wmap, ci, j, di):
        move_y(wmap, ci, j, di, checkonly=False)
        wmap[ci][j] = wmap[i][j]
        wmap[i][j] = "."
        return True
    elif wmap[i][j] == "[" and move_y(wmap, ci, j, di, checkonly) and move_y(wmap, ci, j + 1, di, checkonly):
        if not checkonly:
            move_y(wmap, ci, j, di, checkonly=False)
            move_y(wmap, ci, j + 1, di, checkonly=False)
            wmap[ci][j] = "["
            wmap[ci][j + 1] = "]"
            wmap[i][j] = "."
            wmap[i][j + 1] = "."
        return True
    elif wmap[i][j] == "]" and move_y(wmap, ci, j, di, checkonly) and move_y(wmap, ci, j - 1, di, checkonly):
        if not checkonly:
            move_y(wmap, ci, j, di, checkonly=False)
            move_y(wmap, ci, j - 1, di, checkonly=False)
            wmap[ci][j] = "]"
            wmap[ci][j - 1] = "["
            wmap[i][j] = "."
            wmap[i][j - 1] = "."
        return True

    return False


def solve(wmap, i, j):
    for move in moves:
        if move == "^" and move_y(wmap, i, j, -1):
            i -= 1
        elif move == "v" and move_y(wmap, i, j, 1):
            i += 1
        elif move == "<" and move_x(wmap, i, j, -1):
            j -= 1
        elif move == ">" and move_x(wmap, i, j, 1):
            j += 1

    result = 0
    for i in range(len(wmap)):
        for j in range(len(wmap[0])):
            if wmap[i][j] in ("[", "O"):
                result += i * 100 + j

    print(result)


# Part 1
wmap = [list(l) for l in wmap_raw.split()]
ri, rj = next((i, row.index("@")) for i, row in enumerate(wmap) if "@" in row)
solve(wmap, ri, rj)

# Part 2
wmap = wmap_raw.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
wmap = [list(l) for l in wmap.split()]
ri, rj = next((i, row.index("@")) for i, row in enumerate(wmap) if "@" in row)
solve(wmap, ri, rj)
