total = 0.0

while True:
    line = input()
    if line == "NoMoreMoney":
        break
    amount = float(line)
    if amount < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {amount:.2f}")
    total += amount

print(f"Total: {total:.2f}")