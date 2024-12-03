import re

with open("input.txt", "r") as file:
    instructions = ""
    for instruction in file:
        instructions = instructions + instruction

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, instructions)

total = 0
for match in matches:
    match = match.lstrip("mul(").rstrip(")")
    match = match.split(",")
    total += int(match[0]) * int(match[1])

print(f"The answer is: {total}")
