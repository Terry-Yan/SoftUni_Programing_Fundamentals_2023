number_of_lines = int(input())
keyword = input()
list_of_words = []
list_of_filtered_words = []

for _ in range(number_of_lines):
    new_word = input()
    list_of_words.append(new_word)

    if keyword in new_word:
        list_of_filtered_words.append(new_word)

print(list_of_words)
print(list_of_filtered_words)
