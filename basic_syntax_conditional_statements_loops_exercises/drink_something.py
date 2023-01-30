age = int(input())

if age in range (0, 15):
    print("drink toddy")
elif age in range (15, 19):
    print("drink coke")
elif age in range (18, 22):
    print("drink beer")
elif age > 21:
    print("drink whisky")
