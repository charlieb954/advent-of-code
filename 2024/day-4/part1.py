def check_foward(wordsearch: list) -> int:
    counter = 0
    for row in wordsearch:
        for char_idx, _ in enumerate(row, 0):
            if char_idx + 3 <= len(row):
                if row[char_idx : char_idx + 4] == list("XMAS"):
                    counter += 1

    return counter


def check_backward(wordsearch: list) -> int:
    counter = 0
    for row in wordsearch:
        for char_idx, _ in enumerate(row, 0):
            if char_idx >= 3:
                if row[char_idx - 3 : char_idx + 1][::-1] == list("XMAS"):
                    counter += 1

    return counter


def check_above(wordsearch: list) -> int:
    counter = 0
    for row_idx, row in enumerate(wordsearch, 0):
        for char_idx, _ in enumerate(row, 0):
            if row_idx >= 3:
                potential_word = [
                    wordsearch[row_idx][char_idx],
                    wordsearch[row_idx - 1][char_idx],
                    wordsearch[row_idx - 2][char_idx],
                    wordsearch[row_idx - 3][char_idx],
                ]
                if potential_word == list("XMAS"):
                    counter += 1
    return counter


def check_below(wordsearch: list) -> int:
    counter = 0
    for row_idx, row in enumerate(wordsearch, 0):
        for char_idx, _ in enumerate(row, 0):
            if row_idx + 4 <= len(wordsearch):
                potential_word = [
                    wordsearch[row_idx][char_idx],
                    wordsearch[row_idx + 1][char_idx],
                    wordsearch[row_idx + 2][char_idx],
                    wordsearch[row_idx + 3][char_idx],
                ]
                if potential_word == list("XMAS"):
                    counter += 1

    return counter


def check_diagnal_above_left(wordsearch: list) -> int:
    counter = 0
    for row_idx, row in enumerate(wordsearch, 0):
        for char_idx, _ in enumerate(row, 0):
            if row_idx > 3:
                potential_word = [
                    wordsearch[row_idx][char_idx],
                    wordsearch[row_idx - 1][char_idx - 1],
                    wordsearch[row_idx - 2][char_idx - 2],
                    wordsearch[row_idx - 3][char_idx - 3],
                ]
                if potential_word == list("XMAS"):
                    counter += 1
    return counter


def check_diagnal_above_right(wordsearch: list) -> int:
    counter = 0
    for row_idx, row in enumerate(wordsearch, 0):
        for char_idx, _ in enumerate(row, 0):
            if row_idx >= 3 and char_idx + 3 < len(row):
                potential_word = [
                    wordsearch[row_idx][char_idx],
                    wordsearch[row_idx - 1][char_idx + 1],
                    wordsearch[row_idx - 2][char_idx + 2],
                    wordsearch[row_idx - 3][char_idx + 3],
                ]
                if potential_word == list("XMAS"):
                    counter += 1
    return counter


def check_diagnal_below_left(wordsearch: list) -> int:
    counter = 0
    for row_idx, row in enumerate(wordsearch, 0):
        for char_idx, _ in enumerate(row, 0):
            if row_idx + 3 < len(wordsearch) and char_idx - 3 >= 0:
                potential_word = [
                    wordsearch[row_idx][char_idx],
                    wordsearch[row_idx + 1][char_idx - 1],
                    wordsearch[row_idx + 2][char_idx - 2],
                    wordsearch[row_idx + 3][char_idx - 3],
                ]
                if potential_word == list("XMAS"):
                    counter += 1
    return counter


def check_diagnal_below_right(wordsearch: list) -> int:
    counter = 0
    for row_idx, row in enumerate(wordsearch, 0):
        for char_idx, _ in enumerate(row, 0):
            if row_idx + 3 < len(wordsearch) and char_idx + 3 < len(row):
                potential_word = [
                    wordsearch[row_idx][char_idx],
                    wordsearch[row_idx + 1][char_idx + 1],
                    wordsearch[row_idx + 2][char_idx + 2],
                    wordsearch[row_idx + 3][char_idx + 3],
                ]
                if potential_word == list("XMAS"):
                    counter += 1
    return counter


with open("input.txt") as f:
    wordsearch = []
    for row in f.readlines():
        row = list(row.strip())
        wordsearch.append(row)


total = (
    check_foward(wordsearch)
    + check_backward(wordsearch)
    + check_above(wordsearch)
    + check_below(wordsearch)
    + check_diagnal_above_left(wordsearch)
    + check_diagnal_above_right(wordsearch)
    + check_diagnal_below_left(wordsearch)
    + check_diagnal_below_right(wordsearch)
)

print(f"The answer is: {total}")
