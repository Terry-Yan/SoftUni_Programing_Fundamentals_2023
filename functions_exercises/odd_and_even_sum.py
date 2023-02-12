number = int(input())


def sum_of_digits(n):
    num_string = str(n)
    odd_sum = 0
    even_sum = 0

    for index in range(len(num_string)):
        digit = int(num_string[index])
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return [odd_sum, even_sum]


results = sum_of_digits(number)
print(f"Odd sum = {results[0]}, Even sum = {results[1]}")
