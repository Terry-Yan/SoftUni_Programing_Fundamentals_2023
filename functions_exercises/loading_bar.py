def loading(x):
    loading_bar = ["."] * 10
    max_index = int(x / 10)

    for index in range(max_index):
        loading_bar[index] = "%"

    loading_bar_string = "".join(loading_bar)
    return loading_bar_string


number = int(input())
result = loading(number)
if number == 100:
    print("100% Complete!")
    print(f"[{result}]")
else:
    print(f"{number}% [{result}]")
    print("Still loading...")
