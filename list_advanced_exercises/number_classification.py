line_of_numbers = [int(number) for number in input().split(", ")]
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

[positive_numbers.append(number) if number >= 0 else negative_numbers.append(number) for number in line_of_numbers]
[even_numbers.append(number) if number % 2 == 0 else odd_numbers.append(number) for number in line_of_numbers]
print("Positive:", ', '.join(map(str, positive_numbers)))
print("Negative:", ', '.join(map(str, negative_numbers)))
print("Even:", ', '.join(map(str, even_numbers)))
print("Odd:", ', '.join(map(str, odd_numbers)))
