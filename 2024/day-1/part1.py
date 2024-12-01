list_1, list_2 = [], []

with open("input.txt", "r") as file:
    for line in file:
        first, second = line.strip().split("   ")
        list_1.append(int(first))
        list_2.append(int(second))

list_1 = sorted(list_1)
list_2 = sorted(list_2)

result = [abs(first - second) for first, second in zip(list_1, list_2)]

print(f"The result is: {sum(result)}")
