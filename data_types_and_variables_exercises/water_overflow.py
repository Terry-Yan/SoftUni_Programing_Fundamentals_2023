tank_capacity = 255
number_of_lines = int(input())
liters_taken = 0

for _ in range(number_of_lines):
    liters_income = int(input())

    if tank_capacity >= liters_income:
        tank_capacity -= liters_income
        liters_taken += liters_income
    else:
        print("Insufficient capacity!")

print(liters_taken)
