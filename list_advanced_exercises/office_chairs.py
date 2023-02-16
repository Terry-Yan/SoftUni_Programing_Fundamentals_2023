rooms = int(input())
game_on_flag = True
free_chairs = 0

for room in range(1, rooms + 1):
    room_entry = input().split()
    chairs = len(room_entry[0])
    people = int(room_entry[1])

    if chairs < people:
        missing_chairs = abs(chairs - people)
        print(f"{missing_chairs} more chairs needed in room {room}")
        game_on_flag = False
    else:
        free_chairs += chairs - people

if game_on_flag:
    print(f"Game On, {free_chairs} free chairs left")