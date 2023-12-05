# Part 1
# What would your total score be if everything goes exactly according to your strategy guide?

with open("./input.txt", "r") as f:
    input_list = f.read().split("\n")

a = x = "rock"
b = y = "paper"
c = z = "scissors"

x_rock = 1
y_paper = 2
z_scissors = 3

win = 6
loss = 0
draw = 3

total_score = 0

for row in input_list:
    opponent, my_pick = row.split(" ")
    if my_pick == "X":
        if opponent == "A":
            score = draw + x_rock
        elif opponent == "B":
            score = loss + x_rock
        else:
            score = win + x_rock

    elif my_pick == "Y":
        if opponent == "A":
            score = win + y_paper
        elif opponent == "B":
            score = draw + y_paper
        else:
            score = loss + y_paper

    else:
        if opponent == "A":
            score = loss + z_scissors
        elif opponent == "B":
            score = win + z_scissors
        else:
            score = draw + z_scissors
    
    total_score += score

print(total_score)

# Part 2
# what would your total score be if everything goes exactly according to your new strategy guide?
total_score = 0

for row in input_list:
    opponent, my_pick = row.split(" ")
    if my_pick == "Z": # WIN (Y)
        if opponent == "A": # ROCK 
            score = y_paper + win
        elif opponent == "B": # PAPER
            score = z_scissors + win
        else: # SCISSORS
            score = x_rock + win
    elif my_pick == "Y": # DRAW (X)
        if opponent == "A":
            score = x_rock + draw
        elif opponent == "B":
            score = y_paper + draw
        else:
            score = z_scissors + draw
    else: # LOSS (Z)
        if opponent == "A":
            score = z_scissors
        elif opponent == "B":
            score = x_rock
        else:
            score = y_paper

    total_score += score

print(total_score)
