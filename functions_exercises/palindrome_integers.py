numbers = input().split(", ")


def palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False


for value in numbers:
    print(palindrome(value))
