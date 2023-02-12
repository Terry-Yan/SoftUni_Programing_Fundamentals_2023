password = input()


def validate_password(word):
    valid_flag = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        valid_flag = False

    right_symbols_flag = True
    numbers_counter = 0
    for index in range(len(word)):
        ascii_value = ord(word[index])
        if (0 <= ascii_value <= 47) or (58 <= ascii_value <= 64) or (91 <= ascii_value <= 96) or \
                (123 <= ascii_value <= 127):
            right_symbols_flag = False

        if 48 <= ascii_value <= 57:
            numbers_counter += 1

    if not right_symbols_flag:
        print("Password must consist only of letters and digits")
        valid_flag = False

    if numbers_counter < 2:
        print("Password must have at least 2 digits")
        valid_flag = False

    if valid_flag:
        print("Password is valid")


validate_password(password)
