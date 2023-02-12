product_type = input()
quantity_of_product = int(input())


def order(product, quantity):
    order_value = 0

    if product == "coffee":
        order_value = quantity * 1.50
    elif product == "water":
        order_value = quantity * 1.00
    elif product == "coke":
        order_value = quantity * 1.40
    elif product == "snacks":
        order_value = quantity * 2.00

    return order_value


cost = order(product_type, quantity_of_product)
print(f"{cost:.2f}")
