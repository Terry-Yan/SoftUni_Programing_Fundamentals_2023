to_do_list = [0] * 10

while True:
    entry = input().split("-")
    command = entry[0]

    if command == "End":
        break

    index = int(entry[0]) - 1
    value_str = entry[1]

    to_do_list.pop(index)
    to_do_list.insert(index, value_str)

result = [element for element in to_do_list if element != 0]
print(result)
