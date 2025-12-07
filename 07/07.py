from operator import __mul__

with open("./07/input.txt", "r") as file:
    lines = file.readlines()

# beams = {lines[0].index("S")}
# splits = 0
# for line in lines[1:]:
#     splitters = {i for i, s in enumerate(line) if s == "^"}
#     collisions = beams.intersection(splitters)
#     splits += len(collisions)
#     new_beams = {c - 1 for c in collisions} | {c + 1 for c in collisions}
#     beams = (beams - collisions) | (new_beams)
# print(splits)

beams = {lines[0].index("S"): 1}
splits = 0
for line in lines[1:]:
    splitters = {i for i, s in enumerate(line) if s == "^"}
    collisions = {b: v for b, v in beams.items() if b in splitters}
    splits += len(collisions)
    new_beams = {}
    for c, v in collisions.items():
        beams.pop(c)
        new_beams[c - 1] = new_beams.get(c - 1, 0) + v
        new_beams[c + 1] = new_beams.get(c + 1, 0) + v
    for nb, v in new_beams.items():
        beams[nb] = beams.get(nb, 0) + v

timelines = sum(beams.values())
print(splits)
print(timelines)
