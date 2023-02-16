sequence_of_numbers =[int(number) for number in input().split(", ")]
number_of_groups = 0
if max(sequence_of_numbers) % 10 == 0:
    number_of_groups = max(sequence_of_numbers) // 10
else:
    number_of_groups = (max(sequence_of_numbers) // 10) + 1

for current_group in range(1, number_of_groups + 1):
    current_group_sequence = []
    for element in sequence_of_numbers:
        if ((current_group * 10) - 9) <= element <= current_group * 10:
            current_group_sequence.append(element)

    print(f"Group of {current_group}0's: {current_group_sequence}")
