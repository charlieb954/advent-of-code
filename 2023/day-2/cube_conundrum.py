# part 1
with open("./input.txt") as f:
    input_file = f.readlines()

maximum_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

ids = set()
ids_to_remove = set()

for line in input_file:
    game_id, games = line.split(":")
    *_, game_id = game_id.split(" ")
    ids.add(game_id)
    games = games.split("; ")
    
    game_rows = [ game.strip().split(', ') for game in games ]
    for row in game_rows:
        for col in row:
            count, colour = col.split(" ")
            if int(count) > maximum_cubes[colour]:
                ids_to_remove.add(game_id)

total = sum([int(game_id) for game_id in ids.difference(ids_to_remove)])
print(f"part 1 answer: {total}")


# part 2 -- IN PROGRESS
with open("./input.txt") as f:
    input_file = f.readlines()

total = 0

for line in input_file:
    game_id, games = line.split(":")
    games = games.split("; ")
    game_rows = [ game.strip().split(', ') for game in games ]
    
    for row in game_rows:
        min_cubes = {
            "red": 100,
            "green": 100,
            "blue": 100
        }
        for col in row:
            count, colour = col.split(" ")
            if int(count) < min_cubes[colour]:
                min_cubes[colour] = int(count)
    
    for k, v in min_cubes.items():
        if min_cubes[k] == 100:
            min_cubes[k] = 1
    power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
    total += power

print(f"part 2 answer: {total}")