with open("input.txt") as f:
    input_map = [list(line.strip()) for line in f.readlines()]


def rotate_marker_90(marker: str) -> str:
    marker_lookup = {">": "v", "v": "<", "<": "^", "^": ">"}
    return marker_lookup[marker]


def find_marker():
    for row_idx, row in enumerate(input_map):
        for marker in markers:
            if marker in row:
                return (row.index(marker), row_idx, marker)


def count_map(input_map: list[list]):
    counter = 0
    for row in input_map:
        counter += row.count("X")

    counter += 1  # because he needs to get out!
    return counter


markers = "<^>v"

marker_idx, row_idx, marker = find_marker()

while True:
    marker_idx, row_idx, marker = find_marker()

    if any(
        [
            marker_idx == len(input_map[row_idx]),
            marker_idx == 0,
            row_idx == len(input_map[row_idx]),
            row_idx == 0,
        ]
    ):
        break

    if marker == "^":
        if input_map[row_idx - 1][marker_idx] == "#":
            input_map[row_idx][marker_idx] = rotate_marker_90(marker)
        else:
            input_map[row_idx][marker_idx] = "X"
            input_map[row_idx - 1][marker_idx] = marker

    if marker == ">":
        if input_map[row_idx][marker_idx + 1] == "#":
            input_map[row_idx][marker_idx] = rotate_marker_90(marker)
        else:
            input_map[row_idx][marker_idx] = "X"
            input_map[row_idx][marker_idx + 1] = marker

    if marker == "v":
        if input_map[row_idx + 1][marker_idx] == "#":
            input_map[row_idx][marker_idx] = rotate_marker_90(marker)
        else:
            input_map[row_idx][marker_idx] = "X"
            input_map[row_idx + 1][marker_idx] = marker

    if marker == "<":
        if input_map[row_idx][marker_idx - 1] == "#":
            input_map[row_idx][marker_idx] = rotate_marker_90(marker)
        else:
            input_map[row_idx][marker_idx] = "X"
            input_map[row_idx][marker_idx - 1] = marker


result = count_map(input_map)

print(f"The answer is {result}")
