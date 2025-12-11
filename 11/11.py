from functools import lru_cache

with open("./11/input.txt", "r") as file:
    lines = file.readlines()
    connections = {line[:3]: {l for l in line[4:].strip().split(" ")} for line in lines}
    connections |= {"out": set()}


@lru_cache
def dfs(start: str, end: str) -> int:
    if start == end:
        return 1
    return sum(dfs(server, end) for server in connections[start])


# Part 1


total = dfs("you", "out")
print(total)


# Part 2 - dfs("dac", "fft") = 0

fft = dfs("svr", "fft")
dac = dfs("fft", "dac")
out = dfs("dac", "out")
total = fft * dac * out
print(total)
