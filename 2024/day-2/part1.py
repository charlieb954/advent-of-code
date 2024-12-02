with open("input.txt", "r") as file:
    levels = []
    for level in file:
        levels.append(level.strip().split(" "))

counter = 0

for level in levels:
    level = [int(num) for num in level]
    all_decreasing = all([level[idx] > level[idx+1] for idx in range(len(level[:-1]))])
    all_increasing = all([level[idx] < level[idx+1] for idx in range(len(level[:-1]))])

    if all_increasing or all_decreasing:
        differences = [abs(level[idx] - level[idx+1]) for idx in range(len(level[::-1][:-1]))]
        min_difference = min(differences)
        max_difference = max(differences)

        if min_difference >= 1 and max_difference <= 3:
            counter += 1

print(f"The answer is: {counter}")
