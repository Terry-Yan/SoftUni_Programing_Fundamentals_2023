elements = input().split()
counter = 0

while True:
    line = input()

    if line == "end":
        print("Sorry you lose :(")
        print(*elements)
        break

    counter += 1
    line_args = line.split()
    first_index = int(line_args[0])
    second_index = int(line_args[1])

    if first_index == second_index or first_index < 0 or (first_index > len(elements) - 1) or (second_index < 0) or \
            (second_index > len(elements) - 1):
        midpoint = len(elements) // 2
        elements = elements[0:midpoint] + [f"-{counter}a"] + [f"-{counter}a"] + elements[midpoint:]
        print("Invalid input! Adding additional elements to the board")
        continue

    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        smallest_index = min(first_index, second_index)
        largest_index = max(first_index, second_index)
        elements.pop(smallest_index)
        elements.pop(largest_index - 1)

    else:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {counter} turns!")
        exit()
