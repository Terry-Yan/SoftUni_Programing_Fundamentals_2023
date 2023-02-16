input_values = input().split()
searched_palindrome = input()
palindromes_found = []

for entry in input_values:
    if entry == entry[::-1]:
        palindromes_found.append(entry)

print(palindromes_found)
palindromes_count = palindromes_found.count(searched_palindrome)
print(f"Found palindrome {palindromes_count} times")
