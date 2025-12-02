with open("input.txt") as f:
    ranges = f.read().split(",")

invalid_ids = list()

for r in ranges:
    start, end = map(int, r.split("-"))

    for i in range(start, end + 1):
        i = str(i)
        if len(i) % 2 == 0:
            if i[: int(len(i) / 2)] == i[int(len(i) / 2) :]:
                invalid_ids.append(int(i))

sum_invalid_ids = sum(invalid_ids)

print(f"The answer is {sum_invalid_ids}")
