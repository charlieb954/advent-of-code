# Part 1
# In how many assignment pairs does one range fully contain the other?

with open("./input.txt", "r") as f:
    input_list = f.read().split("\n")

split_input_list = [ row.split(",") for row in input_list ]

counter = 0
for (ass_1, ass_2) in split_input_list:
    ass_1_lower, ass_1_upper = ass_1.split("-")
    ass_2_lower, ass_2_upper = ass_2.split("-")

    ass_1_lower, ass_1_upper = int(ass_1_lower), int(ass_1_upper)
    ass_2_lower, ass_2_upper = int(ass_2_lower), int(ass_2_upper)

    if ((ass_1_lower >= ass_2_lower) and (ass_1_upper <= ass_2_upper)) or ((ass_2_lower >= ass_1_lower) and (ass_2_upper <= ass_1_upper)):
        counter += 1

print(f"Number of pairs that one range fully contains the other {counter}")

# Part 2
# In how many assignment pairs do the ranges overlap?

counter = 0
for (ass_1, ass_2) in split_input_list:
    ass_1_lower, ass_1_upper = ass_1.split("-")
    ass_2_lower, ass_2_upper = ass_2.split("-")

    ass_1_lower, ass_1_upper = int(ass_1_lower), int(ass_1_upper)
    ass_2_lower, ass_2_upper = int(ass_2_lower), int(ass_2_upper)

    range_set_1 = set(range(ass_1_lower, ass_1_upper+1))
    range_set_2 = set(range(ass_2_lower, ass_2_upper+1))

    if len(range_set_1 & range_set_2) > 0:
        counter += 1

print(f"Number of pairs that overlap: {counter}")