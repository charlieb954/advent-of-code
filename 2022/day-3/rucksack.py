# Part 1
# Find the item type that appears in both compartments of each rucksack. 
# What is the sum of the priorities of those item types?
from string import ascii_lowercase, ascii_uppercase

with open("./input.txt", "r") as f:
    input_list = f.read().split("\n")

all_letters = ascii_lowercase + ascii_uppercase

scores = {letter: i for i, letter in enumerate(all_letters, 1)}

total = 0
for row in input_list:
    first_compartment = set(row[:int(len(row)//2)])
    second_compartment = set(row[len(row)//2:])

    priority = list(first_compartment & second_compartment)[0]
    total += scores[priority]

print(f"Sum of the priorities is {total}")

# Part 2
# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
total = 0
for idx in range(0, len(input_list), 3):
    first_compartment = set(input_list[idx])
    second_compartment = set(input_list[idx + 1])
    third_compartment = set(input_list[idx + 2])

    priority = list(first_compartment & second_compartment & third_compartment)[0]
    total += scores[priority]

print(f"Sum of the priorities is {total}")

