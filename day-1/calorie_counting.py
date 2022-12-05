# Part 1
# Find the Elf carrying the most Calories. 
# How many total Calories is that Elf carrying?

with open("./input.txt", "r") as f:
    input_text = f.read()

split_text = input_text.split("\n\n")
nested_split_list = [ temp_list.split("\n") for temp_list in split_text ]
results = [ sum([int(item) for item in temp_list]) for temp_list in nested_split_list ]

print(f"The elf with the most calories is carrying: {max(results)} calories")


# Part 2
# Find the top three Elves carrying the most Calories.
# How many Calories are those Elves carrying in total?
total_top_3 = sum(sorted(results, reverse=True)[:3])

print(f"The top 3 elves carrying the most calories are carrying a total of {total_top_3}")