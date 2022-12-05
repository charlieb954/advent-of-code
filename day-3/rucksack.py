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