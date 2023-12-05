# Part 1
# How many characters need to be processed before the first start-of-packet marker is detected?

with open("input.txt", "r") as f:
    input_text = f.read()

def check_start_packet(num_of_chars=4):
    for idx in range(0, len(input_text)):
        packet = input_text[idx: idx + num_of_chars]
        chars_in_packet = len(set(packet))
        if chars_in_packet == num_of_chars:
            print(f"The first start-of-packet is detected at row {idx+num_of_chars} for {num_of_chars} characters.")
            break

check_start_packet(num_of_chars=4)
check_start_packet(num_of_chars=14)