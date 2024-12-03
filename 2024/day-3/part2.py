import re

with open("input.txt", "r") as file:
    instructions = ""
    for instruction in file:
        instructions = instructions + instruction

pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
matches = re.findall(pattern, instructions)

total = 0
enable = True
for match in matches:
    if match == "don't()":
        enable = False
    elif match == "do()":
        enable = True

    if match != "don't()" and match != "do()":
        if enable:
            match = match.lstrip("mul(").rstrip(")")
            match = match.split(",")
            total += int(match[0]) * int(match[1])

print(f"The answer is: {total}")
