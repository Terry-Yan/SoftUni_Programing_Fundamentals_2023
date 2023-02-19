numbers = [int(x) for x in input().split()]

while True:
    line_args = input().split()
    command = line_args[0]

    if command == "Finish":
        break

    value = int(line_args[1])

    if command == "Add":
        numbers.append(value)

    elif command == "Remove":
        if value in numbers:
            numbers.remove(value)

    elif command == "Replace":
        replacement = int(line_args[2])

        if value in numbers:
            index = numbers.index(value)
            numbers[index] = replacement

    elif command == "Collapse":
        numbers = [x for x in numbers if x >= value]

print(*numbers)
