cipher = input().split()
deciphered = []

for index in range(len(cipher)):
    first_char_code = ""
    current_word = [0]
    for char in cipher[index]:
        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            first_char_code += char
        else:
            current_word.append(char)

    first_char = chr(int(first_char_code))
    current_word[0] = first_char
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    deciphered.append("".join(current_word))

print(" ".join(deciphered))
