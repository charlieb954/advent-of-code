with open("input.txt") as f:
    rotations = f.readlines()

dial = 50
zero_counts = 0

for rotation in rotations:
    direction = rotation[0]
    rotate = int(rotation[1:])

    rotate_hundreds = rotate // 100

    if dial != 0:
        zero_counts += rotate_hundreds
    else:
        zero_counts += rotate_hundreds - 1

    rotate_remainder = rotate % 100

    if direction == "L":
        dial -= rotate_remainder
        if dial < 0:
            dial = 100 - abs(dial)
            if dial != 0:
                zero_counts += 1

    else:
        if dial == 0 and rotate_remainder > 0 and rotate_remainder < 100:
            zero_counts += 1
        dial += rotate_remainder
        if dial >= 100:
            dial = dial - 100
            if dial != 0:
                zero_counts += 1

    if dial == 0:
        zero_counts += 1

print(f"The answer is {zero_counts}")
