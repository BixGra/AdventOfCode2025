from operator import __mul__

with open("./06/input.txt", "r") as file:
    lines = file.readlines()

signs = lines[-1].strip().split()
numbers = [list(map(int, line.strip().split())) for line in lines[:-1]]


def prod(values: list[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def __sum__(a: int, b: int) -> int:
    return a + b


# Part 1

total = 0
for sign, values in zip(signs, zip(*numbers)):
    if sign == "+":
        total += sum(values)
    else:
        total += prod(values)
print(total)


# Part 2

signs = list(lines[-1].rstrip("\n"))
numbers = [list(line.rstrip("\n")) for line in lines[:-1]]
result = 0
total = 0

for sign, values in zip(signs, zip(*numbers)):
    match sign:
        case "*":
            total += result
            result = 1
            f = __mul__
        case "+":
            total += result
            result = 0
            f = __sum__
        case _:
            pass

    if value := "".join(values).strip():
        result = f(result, int(value))
total += result
print(total)
