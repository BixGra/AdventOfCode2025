import re

with open("./02/input.txt", "r") as file:
    lines = file.readlines()

id_ranges = [line.split("-") for line in lines[0].split(",")]

pattern1 = r"-(\d+)(\1)-"
pattern2 = r"-(\d+)(\1+)-"

tmp = (
    "-"
    + "-".join(
        [str(i) for start, end in id_ranges for i in range(int(start), int(end) + 1)]
    )
    + "-"
)
ids1 = re.finditer(pattern1, tmp)
ids2 = re.finditer(pattern2, tmp)
total1 = 0
total2 = 0
for i in ids1:
    total1 += int("".join(i.groups()))
for i in ids2:
    total2 += int("".join(i.groups()))

print(total1)
print(total2)
