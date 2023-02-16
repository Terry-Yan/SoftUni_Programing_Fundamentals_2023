sequence_one = input().split(", ")
sequence_two = input().split(", ")
filtered_sequence = []

for string in sequence_one:
    for big_string in sequence_two:
        if string in big_string:
            filtered_sequence.append(string)
            break

print(filtered_sequence)
