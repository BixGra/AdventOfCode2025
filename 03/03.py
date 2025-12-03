with open("./03/input.txt", "r") as file:
    lines = file.readlines()


def f(line: list[int], size: int, value: int):
    if size == 1:
        return 10 * value + max(line)
    i, v = max(enumerate(line[: -size + 1]), key=lambda x: x[1])
    return f(line[i + 1 :], size - 1, 10 * value + v)


# total = 0
# for line in lines:
#     _line = list(map(int, line.strip()))
#     i, v1 = max(enumerate(_line[:-1]), key=lambda x: x[1])
#     v2 = max(_line[i + 1 :])
#     total += 10 * v1 + v2
# print(total)

total1 = 0
total2 = 0
for line in lines:
    _line = list(map(int, line.strip()))
    total1 += f(_line, 2, 0)
    total2 += f(_line, 12, 0)
print(total1)
print(total2)
