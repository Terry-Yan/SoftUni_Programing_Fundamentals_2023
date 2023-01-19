# Exercise 06:
# Write a program that reads an integer number representing a budget. On the following lines, it reads integer numbers
# representing the prices of each product you should buy until it receives the command "End".
#
# During the iterations, if there is not enough budget left to buy the next product, it prints "You went in overdraft!"
# and end the program.
#
# Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."

budget = int(input())

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    else:
        item_price = int(command)
        if budget - item_price < 0:
            print("You went in overdraft!")
            break
        else:
            budget -= item_price


# Alternative solution:
# budget = int(input())
# command = input()
#
# while command != "End":
#     item_price = int(command)
#     budget -= item_price
#     if budget < 0:
#         print("You went in overdraft!")
#         break
#     command = input()
# else:
#     print("You bought everything needed.")
