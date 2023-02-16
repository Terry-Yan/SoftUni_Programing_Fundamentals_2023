number_of_wagons = int(input())
train = [0] * number_of_wagons

while True:
    entry = input().split()
    command = entry[0]

    if command == "End":
        break

    if command == "add":
        people = int(entry[1])
        train[-1] += people

    elif command == "insert":
        index = int(entry[1])
        people = int(entry[2])
        train[index] += people

    elif command == "leave":
        index = int(entry[1])
        people = int(entry[2])
        train[index] -= people

print(train)
