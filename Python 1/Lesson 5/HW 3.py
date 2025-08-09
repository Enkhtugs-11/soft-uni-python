needed_money = float(input())
available_money = float(input())

consecutive_spend_days = 0
total_days = 0

while True:
    action = input()
    amount = float(input())
    total_days += 1

    if action == "spend":
        available_money -= amount
        if available_money < 0:
            available_money = 0
        consecutive_spend_days += 1
    elif action == "save":
        available_money += amount
        consecutive_spend_days = 0

    if consecutive_spend_days == 5:
        print("You can't save the money.")
        print(f"{total_days}")
        break

    if available_money >= needed_money:
        print(f"You saved the money for {total_days} days.")
        break
