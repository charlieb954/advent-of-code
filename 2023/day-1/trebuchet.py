import re

# part 1
with open("./input.txt") as f:
    input_file = f.readlines()

total = 0
for row in input_file:
    nums = [n for n in row if n.isdigit()]
    first, *_ = nums
    *_, last = nums
    calibration_value = int(first + last)
    total += calibration_value

print(f"part one: {total}")

# part 2
with open("./input.txt") as f:
    input_file = f.readlines()

repl = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

total = 0
for row in input_file:
    row = row.strip()

    exp = re.compile(r"(one|two|three|four|five|six|seven|eight|nine|\d).*$")
    first = exp.search(row).groups()[0]

    exp = re.compile(r"^.*(one|two|three|four|five|six|seven|eight|nine|\d)")
    last = exp.search(row).groups()[0]

    if not first.isdigit():
        first = repl[first]

    if not last.isdigit():
        last = repl[last]

    calibration_value = int(str(first) + str(last))
    total += calibration_value

print(f"part two: {total}")
