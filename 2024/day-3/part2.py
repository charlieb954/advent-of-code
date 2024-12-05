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
    else:
        if enable:
            number_1, number_2 = match.lstrip("mul(").rstrip(")").split(",")
            total += int(number_1) * int(number_2)

print(f"The answer is: {total}")
