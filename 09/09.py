import numpy as np

with open("./09/input.txt", "r") as file:
    lines = file.readlines()


# Part 1


reds = [tuple(map(int, line.strip().split(","))) for line in lines]
x, y = list(zip(*reds))
x = np.array(x)
y = np.array(y)

x_rect = np.abs(x[:, np.newaxis] - x.T) + 1
y_rect = np.abs(y[:, np.newaxis] - y.T) + 1
rects = x_rect * y_rect

total = rects.max()
print(total)


# Part 2

perimeter = set()
for i, (x1, y1) in enumerate(reds):
    for x2, y2 in reds[i + 1 :]:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                perimeter.add((x1, y))
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                perimeter.add((x, y1))

total = 0
for i, (x1, y1) in enumerate(reds):
    for j, (x2, y2) in enumerate(reds[i + 1 :]):
        curr = rects[i, i + j + 1]
        if curr < total:
            continue

        min_x, max_x = sorted([x1, x2])
        min_y, max_y = sorted([y1, y2])
        inside = False
        for xp, yp in perimeter:
            if min_x < xp < max_x and min_y < yp < max_y:
                inside = True
                break
        if not inside:
            total = curr

print(total)
