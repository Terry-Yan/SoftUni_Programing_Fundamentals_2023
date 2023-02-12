numbers = [int(x) for x in input().split(" ")]


def find_the_evens(a):
    if a % 2 == 0:
        return True
    else:
        return False


even_numbers = filter(find_the_evens, numbers)
results = []

for x in even_numbers:
    results.append(x)

print(results)
