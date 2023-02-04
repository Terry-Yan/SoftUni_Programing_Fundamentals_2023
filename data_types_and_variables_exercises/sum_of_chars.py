number_of_chars = int(input())
total_sum = 0

for _ in range(number_of_chars):
    char = input()
    value = ord(char)
    total_sum += value

print(f"The sum equals: {total_sum}")
