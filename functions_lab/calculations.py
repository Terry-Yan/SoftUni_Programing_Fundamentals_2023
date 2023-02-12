operator = input()
first_number = int(input())
second_number = int(input())


def calculations(command, n_1, n_2):
    if command == "multiply":
        return n_1 * n_2
    elif command == "divide":
        return n_1 // n_2
    elif command == "add":
        return n_1 + n_2
    elif command == "subtract":
        return n_1 - n_2


print(calculations(operator, first_number, second_number))
