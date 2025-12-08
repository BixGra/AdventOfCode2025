with open("./08/input.txt", "r") as file:
    lines = file.readlines()

Box = list[tuple[int, int, int]]


def prod(values: list[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def dist(u: Box, v: Box) -> int:
    return sum(map(lambda x: x * x, map(lambda uv: uv[0] - uv[1], zip(u, v))))


boxes: Box = [tuple(map(int, line.strip().split(","))) for line in lines]
dists = {
    (i, i + 1 + j): dist(u, v)
    for i, u in enumerate(boxes[:-1])
    for j, v in enumerate(boxes[i + 1 :])
}
sorted_dists = list(map(lambda d: d[0], sorted(dists.items(), key=lambda x: x[1])))

connected_boxes: dict[int, int] = {}
circuits: dict[int, set] = {}
size = len(boxes)

i = 0
pairs = 1000
condition = False
while not condition:
    if i == pairs:
        total1 = prod(sorted(map(len, circuits.values()), reverse=True)[:3])
    u, v = sorted_dists[i]
    i += 1
    match (u in connected_boxes, v in connected_boxes):
        case (True, True):
            if v in circuits[connected_boxes[u]]:
                continue
            ucircuit = connected_boxes[u]
            vcircuit = connected_boxes[v]
            for box in circuits[vcircuit]:
                connected_boxes[box] = connected_boxes[ucircuit]
            circuits[ucircuit] |= circuits[vcircuit]
            del circuits[vcircuit]
        case (True, False):
            ucircuit = connected_boxes[u]
            connected_boxes[v] = connected_boxes[ucircuit]
            circuits[ucircuit].add(v)
        case (False, True):
            vcircuit = connected_boxes[v]
            connected_boxes[u] = connected_boxes[vcircuit]
            circuits[vcircuit].add(u)
        case _:
            connected_boxes[u] = u
            connected_boxes[v] = u
            circuits[u] = {u, v}
    condition = len(list(circuits.values())[0]) == size

total2 = boxes[u][0] * boxes[v][0]

print(total1)
print(total2)
