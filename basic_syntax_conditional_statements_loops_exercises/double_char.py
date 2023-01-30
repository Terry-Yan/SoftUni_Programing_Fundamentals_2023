command = input()

while command != "End":
    if command == "SoftUni":
        pass
    else:
        for char in range(len(command)):
            print(f"{command[char]}", end="")
            print(f"{command[char]}", end="")
        print()

    command = input()
