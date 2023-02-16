numbers = [int(x) for x in input().split(", ")]
indices = []

for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        indices.append(index)

print(indices)
