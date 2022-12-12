# Part 1
# After the rearrangement procedure completes, what crate ends up on top of each stack

def get_crate_dict() -> dict:
    crate_dict = dict()

    for row in input_list:
        row = [ row[idx:idx + 4].strip() for idx in range(0, len(row), 4) ]
        if row[0] != '1':
            for i in range(1, 10):
                crate_dict[i] = crate_dict.get(i, [])
                if row[i-1] != '':
                    crate_dict[i].insert(0, row[i-1])
        else:
            break
    
    return crate_dict

def summarise_crates(crate_dict) -> str:
    result = [crate_dict[key][-1] for key in crate_dict.keys()]
    result = [res.replace("[", "").replace("]", "") for res in result]

    return "".join(result)


with open("input.txt") as f:
    input_list = f.readlines()

crate_dict = get_crate_dict()

for command in input_list[10:]:
    _, num_crates, _, from_stack, _, to_stack = command.strip().split(' ')
    for idx in range(int(num_crates)):
        crate_dict[int(to_stack)].append(crate_dict[int(from_stack)].pop())

print(summarise_crates(crate_dict))

# Part 2
crate_dict = get_crate_dict()

for command in input_list[10:]:
    _, num_crates, _, from_stack, _, to_stack = command.strip().split(' ')
    crates_to_add = crate_dict[int(from_stack)][len(crate_dict[int(from_stack)])-int(num_crates):]
    del crate_dict[int(from_stack)][len(crate_dict[int(from_stack)])-int(num_crates):]
    crate_dict[int(to_stack)].extend(crates_to_add)

print(summarise_crates(crate_dict))
