number_of_lines = int(input())

for i in range(number_of_lines):
    code_number = int(input())

    if code_number <= 88:
        if code_number == 88:
            print("Hello")
        elif code_number == 86:
            print("How are you?")
        else:
            print("GREAT!")
    else:
        print("Bye.")
