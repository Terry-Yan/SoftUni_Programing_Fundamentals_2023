def factorial_function(a, b):
    fac_a = 1
    fac_b = 1

    for x in range(a, 0, -1):
        fac_a *= x

    for x in range(b, 0, -1):
        fac_b *= x

    division = fac_a / fac_b
    return division


first_number = int(input())
second_number = int(input())

result = factorial_function(first_number, second_number)
print(f"{result:.2f}")
