with open("./05/input.txt", "r") as file:
    lines = file.readlines()


def merge_ranges(id_ranges: list[list[int]]) -> list[list[int]]:
    new = [id_ranges[0]]
    for id_range in id_ranges[1:]:
        curr = new[-1]
        if (curr[0] <= id_range[0] <= curr[1]) or (curr[0] <= id_range[1] <= curr[1]):
            new[-1][1] = max(curr[1], id_range[1])
        else:
            new.append(id_range)
    return new


id_ranges = []
i = 0
length = len(lines)

while lines[i].strip():
    id_ranges.append(list(map(int, lines[i].strip().split("-"))))
    i += 1
id_ranges = sorted(id_ranges, key=lambda x: x[0])
id_ranges = merge_ranges(id_ranges)

i += 1

total = 0
while i < length:
    ingredient = int(lines[i].strip())
    for id_range in id_ranges:
        if ingredient < id_range[0]:
            break
        if id_range[0] <= ingredient <= id_range[1]:
            total += 1
    i += 1

print(total)

total = sum(map(lambda x: x[1] - x[0] + 1, id_ranges))
print(total)
