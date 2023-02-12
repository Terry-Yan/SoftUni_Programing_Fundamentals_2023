numbers_string = input()
string_list = numbers_string.split()
reversed_list = []

for index in range(len(string_list)):
    element = int(string_list[index]) * -1
    reversed_list.append(element)

print(reversed_list)
