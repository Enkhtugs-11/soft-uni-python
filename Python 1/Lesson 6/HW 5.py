N = int(input())

for number in range(1111, 10000):
    num_str = str(number)
    special = True

    for ch in num_str:
        digit = int(ch)
        if digit == 0 or N % digit != 0:
            special = False
            break

    if special:
        print(number, end=' ')
