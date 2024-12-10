from itertools import product


def read_input() -> list:
    with open("input.txt") as f:
        equations = f.readlines()
    return equations


def calculate_combinations(numbers: list[int]) -> list[tuple]:
    """generate all combinations of operations

    Args:
        numbers (list[int]): numbers to get the length of combinations.

    Returns:
        (list[tuple]): generator of tuples showing all combinations.
    """
    ops = ["*", "+", "||"]
    op_combinations = product(ops, repeat=len(numbers))

    return list(op_combinations)


def check_target(combos: list[tuple], numbers: list[int], target: int) -> bool:
    """check if the target is met by any of the combos, if so return True else
    False.

    Args:
        combos (list[tuple]): all possible combinations. 
        numbers (list[int]): the numbers to multiply/add.
        target (int): the target value

    Returns:
        bool: True if the target value is met else False.
    """
    for combo in combos:
        combo = list(combo)
        temp_total = 0

        inital_operator = combo.pop(0)
        if inital_operator == "*":
            temp_total = numbers[0] * numbers[1]
        elif inital_operator == "||":
            temp_total = int(f"{numbers[0]}{numbers[1]}")
        else:
            temp_total = numbers[0] + numbers[1]

        for num in numbers[2:]:
            operator = combo.pop(0)
            if operator == "*":
                temp_total *= num
            elif operator == "||":
                temp_total = int(f"{temp_total}{num}")
            else:
                temp_total += num

        if temp_total == target:
            return True

    return False


def main() -> None:
    equations = read_input()

    counter = 0
    for equation in equations:
        target, numbers = equation.split(":")
        target = int(target)
        numbers = [int(num) for num in numbers.split()]

        combos = calculate_combinations(numbers)

        if check_target(combos, numbers, target):
            counter += target

    print(f"The result is {counter}")

if __name__ == "__main__":
    main()