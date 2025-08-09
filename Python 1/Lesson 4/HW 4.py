N = int(input())
X = float(input())
P = int(input())

toys_count = 0
money_sum = 0.0
money_gift = 10.0

for age in range(1, N + 1):
    if age % 2 == 0:
        money_sum += money_gift
        money_sum -= 1.0
        money_gift += 10.0
    else:
        toys_count += 1

money_sum += toys_count * P

if money_sum >= X:
    print(f"Yes! {money_sum - X:.2f} ")
else:
    print(f"No! {X - money_sum:.2f}")
