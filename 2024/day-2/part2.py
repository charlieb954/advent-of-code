def check_levels(level: list) -> bool:
    """check whether all items are increasing or decreasing and if there is a
    minimum difference of 1 and maximum difference of 3.

    Args:
        level (list): a list of numbers to check

    Returns:
        bool: True if the criteria is met else False
    """
    level = [int(num) for num in level]

    all_decreasing = all(
        [level[idx] > level[idx + 1] for idx in range(len(level[:-1]))]
    )
    all_increasing = all(
        [level[idx] < level[idx + 1] for idx in range(len(level[:-1]))]
    )

    if all_increasing or all_decreasing:
        differences = [
            abs(level[idx] - level[idx + 1]) for idx in range(len(level[::-1][:-1]))
        ]
        min_difference = min(differences)
        max_difference = max(differences)

        if min_difference >= 1 and max_difference <= 3:
            return True
    return False


with open("input.txt", "r") as file:
    levels = [level.strip().split() for level in file]

counter = 0
for level in levels:
    for idx in range(len(level)):
        temp_level = level.copy()
        temp_level.pop(idx)
        if check_levels(temp_level):
            counter += 1
            break

print(f"The answer is: {counter}")
