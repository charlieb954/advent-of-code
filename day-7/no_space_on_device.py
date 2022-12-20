# Part 1
# What is the sum of the total sizes of those directories?
with open("input.txt", "r") as f:
    input_list = f.readlines()
    input_list = [ cmd.strip() for cmd in input_list ]

all_files = []
dirs = []
loc = []

for row in input_list:
    if row == "$ ls" or row.startswith('dir'):
        continue

    elif row.startswith("$"):
        split_row = row.split(" ")
        if len(split_row) == 3:
            _, cmd, location = split_row
            if cmd == "cd" and location != "..":
                loc.append(location)
                dirs.append(location)
            elif cmd == "cd" and location == "..":
                loc.pop()
            else:
                raise Exception()
    else:
        all_files.append("/".join(loc)+"/"+row)

folders = {}
for folder in dirs:
    for row in all_files:
        file_list = ["/"] + [ r for r in row.split("/") if r != "" ]
        if folder in file_list:
            folders[folder] = folders.get(folder, [])
            folders[folder].append(int(file_list[-1].split(' ')[0]))
        
answer = 0
for k, v in folders.items():
    folders[k] = sum(v)
    if folders[k] <= 100_000:
        answer += folders[k]

print(answer)