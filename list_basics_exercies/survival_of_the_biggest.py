list_of_strings = input().split(" ")
list_of_numbers = list(map(int, list_of_strings))
n = int(input())

for _ in range(n):
    value_for_removal = min(list_of_numbers)
    list_of_numbers.remove(value_for_removal)

print(", ".join(str(x) for x in list_of_numbers))
