number_of_entries = int(input())
positive_list = []
negative_list = []

for _ in range(number_of_entries):
    entry = int(input())

    if entry >= 0:
        positive_list.append(entry)
    else:
        negative_list.append(entry)

positive_counter = len(positive_list)
negative_sum = sum(negative_list)

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_counter}")
print(f"Sum of negatives: {negative_sum}")
