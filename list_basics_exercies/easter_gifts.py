gifts_list = input().split(" ")
command = input()
none_counter = 0

while command != "No Money":
    command_list = command.split(" ")

    if command_list[0] == "OutOfStock":
        for index in range(len(gifts_list)):
            if gifts_list[index] == command_list[1]:
                gifts_list[index] = "None"
                none_counter += 1

    elif command_list[0] == "Required":
        index_in_question = int(command_list[2])
        if 0 < index_in_question < len(gifts_list):
            gifts_list[index_in_question] = command_list[1]

    elif command_list[0] == "JustInCase":
        gifts_list[-1] = command_list[1]

    command = input()

for _ in range(none_counter):
    if "None" in gifts_list:
        gifts_list.remove("None")

print(*gifts_list)
