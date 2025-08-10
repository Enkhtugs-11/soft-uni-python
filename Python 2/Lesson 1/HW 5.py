n = int(input())
total = 0

for _ in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())

    if 0.01 <= price <= 100.00 and 1 <= days <= 31 and 1 <= capsules <= 2000:
        order_price = price * days * capsules
        print(f"The price for the coffee is: ${order_price:.2f}")
        total += order_price

print(f"Total: ${total:.2f}")
