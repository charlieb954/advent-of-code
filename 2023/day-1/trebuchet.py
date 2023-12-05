import re

## part 1
with open("./input.txt") as f:
    input_file = f.readlines()

total = 0
for row in input_file:
    nums = [n for n in row if n.isdigit()]
    first, *_ = nums
    *_ , last = nums
    calibration_value = int(first + last)
    total += calibration_value

print(total)

## part 2
# with open("./input.txt") as f:
#     input_file = f.readlines()

input_file = '''eightwothree'''.split('\n')

repl = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

total = 0
for row in input_file:

    print(row)

    nums = []
    
    for char in row:
        if char.isdigit():
            nums.append(char)
    for k, v in repl.items():
        row = re.sub(k, str(v), row)

    nums = [n for n in row if n.isdigit()]
    print(nums)
    first, *_ = nums
    *_ , last = nums
    calibration_value = int(first + last)
    total += calibration_value

print(total)

import re

## part 2
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
    "nine": 9
}

total = 0
for row in input_file:
    
    row = row.strip()
        
    regexp = re.compile("^.*(one|two|three|four|five|six|seven|eight|nine|\d)")
    first = regexp.search(row).groups()[0]

    regexp = re.compile("(one|two|three|four|five|six|seven|eight|nine|\d).*$")
    last = regexp.search(row).groups()[0]
        
    if not first.isdigit():
        first = repl[first]
    
    if not last.isdigit():
        last = repl[last]
    
    calibration_value = int(str(first) + str(last))
    total += calibration_value
    
print(total)