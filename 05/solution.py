with open("./input.txt") as f:
    data = [l.strip() for l in f]

ordering, updates = data[:1176], data[1177:]

part1, part2 = 0, 0
for u in updates:
    correct = True
    nums = u.split(",")
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if f"{nums[j]}|{nums[i]}" in ordering:
                correct = False
                nums[j], nums[i] = nums[i], nums[j]
    if correct:
        part1 += int(nums[len(nums) // 2])
    else:
        part2 += int(nums[len(nums) // 2])

print(part1)
print(part2)
