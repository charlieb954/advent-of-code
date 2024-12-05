import re

with open("input.txt", "r") as file:
    instructions = ""
    for instruction in file:
        instructions = instructions + instruction

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, instructions)

total = 0
for match in matches:
    number_1, number_2 = match.lstrip("mul(").rstrip(")").split(",")
    total += int(number_1) * int(number_2)

print(f"The answer is: {total}")
