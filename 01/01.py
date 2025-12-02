with open("./01/input.txt", "r") as file:
    lines = file.readlines()


# Part 1
zeros = 0
current = 50

# 2 * (0.5 - int(line[0] == "L"))

for line in lines:
    if line[0] == "L":
        current = (current - int(line[1:])) % 100
    else:
        current = (current + int(line[1:])) % 100
    if current == 0:
        zeros += 1
print(zeros)

# Part 2

zeros = 0
current = 50

for line in lines:
    if line[0] == "L":
        sign = -1
    else:
        sign = 1
    current = (sign * current) % 100
    current += int(line[1:])
    zeros += abs(current // 100)
    current = (sign * current) % 100
print(zeros)
