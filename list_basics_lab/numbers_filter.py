number_of_lines = int(input())
numbers_list = []

for _ in range(number_of_lines):
    number = int(input())
    numbers_list.append(number)

command = input()
filtered_list = []

if command == "even":
    for number in numbers_list:
        if number % 2 == 0 or number == 0:
            filtered_list.append(number)
elif command == "odd":
    for number in numbers_list:
        if number % 2 != 0:
            filtered_list.append(number)
elif command == "negative":
    for number in numbers_list:
        if number < 0:
            filtered_list.append(number)
elif command == "positive":
    for number in numbers_list:
        if number >= 0:
            filtered_list.append(number)

print(filtered_list)
