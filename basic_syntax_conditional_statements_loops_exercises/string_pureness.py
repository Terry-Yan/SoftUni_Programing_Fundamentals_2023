n = int(input())

for s in range(n):
    current_string = input()
    pure_flag = True

    for char in range(len(current_string)):
        if current_string[char] == "," or current_string[char] == "." or current_string[char] == "_":
            pure_flag = False
            break

    if pure_flag:
        print(f"{current_string} is pure.")
    else:
        print(f"{current_string} is not pure!")
