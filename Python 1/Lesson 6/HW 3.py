prime_sum = 0
non_prime_sum = 0

while True:
    user_input = input()

    if user_input.lower() == "stop":
        break

    is_valid_number = True
    if user_input.startswith('-'):
        if not user_input[1:].isdigit():
            is_valid_number = False
    elif not user_input.isdigit():
        is_valid_number = False

    if not is_valid_number:
        print("Invalid input. Please enter an integer or 'stop'.")
        continue

    number = int(user_input)

    if number < 0:
        print("Number is negative.")
        continue

    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for i in range(2, number):
            for j in range(1):
                if number % i == 0:
                    is_prime = False
                    break
            if not is_prime:
                break

    if is_prime:
        prime_sum += number
    else:
        non_prime_sum += number

print("Sum of all prime numbers is:", prime_sum)
print("Sum of all non prime numbers is:", non_prime_sum)
