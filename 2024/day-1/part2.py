from collections import Counter


with open("input.txt", "r") as file:
    list_1, list_2 = [], []
    for line in file:
        first, second = line.strip().split()
        list_1.append(int(first))
        list_2.append(int(second))

value_counts = Counter(list_2)
unique_numbers = set(list_1)

total = 0
for number in unique_numbers:
    similarity_score = number * value_counts.get(number, 0)
    total += similarity_score

print(f"The result is: {total}")
