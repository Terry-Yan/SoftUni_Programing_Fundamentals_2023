first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(c, d):
    return c - d


def add_and_subtract(x, y, z):
    sum_number = sum_numbers(x, y)

    subtract_numbers = subtract(sum_number, z)
    return subtract_numbers


print(add_and_subtract(first_number, second_number, third_number))
