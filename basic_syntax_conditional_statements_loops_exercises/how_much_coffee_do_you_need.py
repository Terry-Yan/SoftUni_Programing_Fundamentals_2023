command = input()
total_coffee = 0

while command != "END":
    upper_string_flag = False

    if command.lower() in ["coding", "dog", "cat", "movie"]:
        for char in command:
            if char.isupper():
                upper_string_flag = True
                break

        if upper_string_flag:
            total_coffee += 2
        else:
            total_coffee += 1

        command = input()
    else:
        command = input()

if total_coffee > 5:
    print("You need extra sleep")
else:
    print(total_coffee)
