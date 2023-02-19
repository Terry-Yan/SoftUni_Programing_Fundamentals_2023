cards = input().split(", ")
number_of_lines = int(input())

for _ in range(number_of_lines):
    line_args = input().split(", ")
    command = line_args[0]

    if command == "Add":
        card_name = line_args[1]
        if card_name not in cards:
            cards.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")

    elif command == "Remove":
        card_name = line_args[1]

        if card_name not in cards:
            print("Card not found")
        else:
            cards.remove(card_name)
            print("Card successfully removed")

    elif command == "Remove At":
        index = int(line_args[1])

        if index not in range(0, len(cards)):
            print("Index out of range")
        else:
            cards.pop(index)
            print("Card successfully removed")

    elif command == "Insert":
        index = int(line_args[1])
        card_name = line_args[2]

        if index not in range(0, len(cards)):
            print("Index out of range")
        elif card_name in cards:
            print("Card is already added")
        else:
            cards.insert(index, card_name)
            print("Card successfully added")

print(", ".join(cards))
