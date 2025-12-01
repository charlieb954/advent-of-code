with open("input.txt") as f:
    rotations = f.readlines()

dial = 50
zero_counts = 0

for rotation in rotations:
    direction = rotation[0]
    rotate = rotation[1:]

    # ignore the hundreds place if it exists
    if len(rotate) == 2:
        rotate = int(rotate)
    else:
        rotate = int(rotate[-3:])

    if direction == "L":
        dial -= rotate
        if dial < 0:
            dial = 100 - abs(dial)

    else:
        dial += rotate
        if dial >= 100:
            dial = dial - 100

    if dial == 0:
        zero_counts += 1

print(f"The answer is {zero_counts}")
