max_health = 100
bitcoins = 0
current_health = max_health
dungeon = input().split("|")
death_flag = False

for room_number in range(len(dungeon)):
    room_args = dungeon[room_number].split(" ")
    command = room_args[0]
    value = int(room_args[1])

    if command == "potion":
        health_healed = 0

        if current_health + value > max_health:
            health_healed = max_health - current_health
            current_health = max_health
        else:
            health_healed = value
            current_health += value

        print(f"You healed for {health_healed} hp.")
        print(f"Current health: {current_health} hp.")

    elif command == "chest":
        print(f"You found {value} bitcoins.")
        bitcoins += value
    else:
        monster = command
        attack = value
        current_health -= attack

        if current_health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_number + 1}")
            death_flag = True
            break

if not death_flag:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {current_health}")
