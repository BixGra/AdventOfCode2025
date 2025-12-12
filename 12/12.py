with open("./12/input.txt", "r") as file:
    lines = file.readlines()

presents = [[line.strip() for line in lines[5 * i + 1 : 5 * i + 4]] for i in range(6)]
areas = [sum(q == "#" for p in present for q in p) for present in presents]

sections = [
    (
        tuple(int(i) for i in section[0].split("x")),
        tuple(int(i) for i in section[1].split()),
    )
    for section in [line.strip().split(": ") for line in lines[30:]]
]

total = 0
for (x, y), section in sections:
    total_area = x * y
    presents_area = sum(area * s for area, s in zip(areas, section))
    if presents_area < total_area:
        total += 1
print(total)
