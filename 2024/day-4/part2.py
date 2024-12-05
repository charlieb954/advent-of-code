with open("input.txt") as f:
    wordsearch = [list(row.strip()) for row in f.readlines()]

total = 0
for row_idx, row in enumerate(wordsearch):
    # skip the first and last row
    if row_idx == 0 or row_idx == len(wordsearch) - 1:
        continue
    for char_idx, char in enumerate(row):
        # if first character then the A can't be in the centre of the MAS
        if char_idx > 0:
            if char == "A" and char_idx + 1 < len(row):

                # get the other 4 characters surrounding the "A"
                top_left = wordsearch[row_idx - 1][char_idx - 1]
                top_right = wordsearch[row_idx - 1][char_idx + 1]
                bottom_left = wordsearch[row_idx + 1][char_idx - 1]
                bottom_right = wordsearch[row_idx + 1][char_idx + 1]

                # check for the combinations that make MAS
                if (top_right == "S" and bottom_left == "M") or (top_right == "M" and bottom_left == "S"):                
                    if (top_left == "S" and bottom_right == "M") or (top_left == "M" and bottom_right == "S"):
                        total += 1


print(f"The answer is: {total}")
