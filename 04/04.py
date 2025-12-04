import numpy as np
from scipy.signal import convolve2d

with open("./04/input.txt", "r") as file:
    lines = file.readlines()

matrix = np.array([list(map(lambda x: int(x == "@"), line.strip())) for line in lines])
kernel = np.array([[-1, -1, -1], [-1, 4, -1], [-1, -1, -1]])

# Part 1
total = 0
convoluted = convolve2d(matrix, kernel, mode="same", boundary="fill", fillvalue=0)
result: np.ndarray = (convoluted > 0).astype(int)
total += result.sum()
print(total)

# Part 2
while result.sum():
    matrix -= result
    convoluted = convolve2d(matrix, kernel, mode="same", boundary="fill", fillvalue=0)
    result: np.ndarray = (convoluted > 0).astype(int)
    total += result.sum()
print(total)
