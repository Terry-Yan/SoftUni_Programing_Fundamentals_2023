number_of_people = int(input())
capacity = int(input())

courses = number_of_people // capacity
left_over = number_of_people % capacity

if courses == 0:
    print("1")
elif left_over == 0:
    print(f"{courses}")
else:
    print(f"{courses + 1}")
