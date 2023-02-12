first_number = int(input())
second_number = int(input())
third_number = int(input())


def find_the_smallest_number(a, b, c):
    input_list = [a, b, c]
    return min(input_list)


print(find_the_smallest_number(first_number, second_number, third_number))
