with open("./input.txt") as f:
    diskmap = list(map(int, f.read()))

disk, free_space, files = [], [], []
i = 0
for j, size in enumerate(diskmap):
    if j % 2 == 0:
        val = j // 2
        files.append((val, i, i + size))
    else:
        val = None
        free_space.append((i, i + size))
    disk += [val] * size
    i += size


def part1(disk):
    free_space_idx, file_idx = 0, len(disk) - 1
    while free_space_idx < file_idx:
        if disk[free_space_idx] is not None:
            free_space_idx += 1
            continue

        if disk[file_idx] is None:
            file_idx -= 1
            continue

        disk[free_space_idx], disk[file_idx] = disk[file_idx], disk[free_space_idx]

    result = sum(i * fid for i, fid in enumerate(disk) if fid is not None)
    print(result)


def part2(disk):
    for fid, file_start, file_end in files[::-1]:
        file_size = file_end - file_start
        for i in range(len(free_space)):
            free_space_start, free_space_end = free_space[i]
            if free_space_start > file_start:
                break
            free_space_size = free_space_end - free_space_start
            if free_space_size < file_size:
                continue

            disk[file_start:file_end] = [None] * file_size
            disk[free_space_start:free_space_start + file_size] = [fid] * file_size
            free_space[i] = (free_space_start + file_size, free_space_end)
            break

    result = sum(i * fid for i, fid in enumerate(disk) if fid is not None)
    print(result)


part1(disk[:])
part2(disk[:])
