user_input = input()
max_number = -1000000000000

while user_input != "Stop":
    num = int(user_input)

    if num > max_number:
        max_number = num

    user_input = input()

print(max_number)
