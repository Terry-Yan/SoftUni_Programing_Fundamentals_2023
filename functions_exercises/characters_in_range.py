first_char = input()
second_char = input()


def ascii_string(a, b):
    the_string = ""
    start_index = ord(a)
    end_index = ord(b)

    for index in range(start_index + 1, end_index):
        char = chr(index)
        the_string += char + " "

    return the_string


all_char = ascii_string(first_char, second_char)
print(all_char)
