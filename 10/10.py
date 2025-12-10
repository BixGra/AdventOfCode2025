from itertools import combinations

import numpy as np

with open("./10/input.txt", "r") as file:
    lines = file.readlines()

all_lights: list[np.ndarray] = []
all_buttons = []
all_joltages: list[np.ndarray] = []

for line_ in lines:
    line = line_.strip("\n")
    lights, line = line.split(" ", 1)
    all_lights.append(np.array([int(light == "#") for light in lights[1:-1]]))
    buttons, joltages = line.rsplit(" ", 1)
    all_buttons.append(
        [[int(b) for b in button[1:-1].split(",")] for button in buttons.split(" ")]
    )
    all_joltages.append(
        np.array([int(joltage) for joltage in joltages[1:-1].split(",")])
    )

all_states: list[np.ndarray] = [
    np.array([[int(i in button) for i in range(len(lights))] for button in buttons])
    for lights, buttons in zip(all_lights, all_buttons)
]


# Part 1


total = 0
for lights, states in zip(all_lights, all_states):
    presses = 1
    found = False
    while not found:
        for combination in combinations(states, presses):
            if (lights == sum(combination) % 2).all():
                found = True
                total += presses
                break
        presses += 1
print(total)


# Part 2


# def partitions(n, k):
#     for c in combinations(range(n + k - 1), k - 1):
#         yield [b - a - 1 for a, b in zip((-1,) + c, c + (n + k - 1,))]
# total = 0
# for joltages, states in zip(all_joltages, all_states):
#     presses = max(joltages)
#     found = False
#     while not found:
#         for combination in partitions(presses, states.shape[0]):
#             coefficients = np.array([combination])
#             if (joltages == np.dot(coefficients, states)).all():
#                 found = True
#                 total += presses
#                 break
#         presses += 1
# print(total)


from z3 import *

total = 0
for joltages, states in zip(all_joltages, all_states):
    presses = Int("presses")
    coefficients = [Int(f"coefficient_{i}") for i in range(states.shape[0])]

    equations = []
    for joltage, state in zip(joltages, states.T):
        equations.append(sum([c * s for c, s in zip(coefficients, state)]) == joltage)
    for coefficient in coefficients:
        equations.append(coefficient >= 0)
    equations.append(presses == sum(coefficients))

    solver = Optimize()
    solver.add(equations)
    solver.minimize(presses)
    solver.check()

    total += solver.model()[presses].as_long()
print(total)
