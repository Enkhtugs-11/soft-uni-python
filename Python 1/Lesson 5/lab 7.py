user_input = input()
min_number = None

while user_input != "Stop":
    number = int(user_input)

    if min_number is None or number < min_number:
        min_number = number

    user_input = input()

print(min_number)
