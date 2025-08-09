budget = float(input())
extras = int(input())
price_per_clothing = float(input())

decor_cost = budget * 0.10

clothing_cost = extras * price_per_clothing

if extras > 150:
    clothing_cost *= 0.90

total_cost = decor_cost + clothing_cost

diff = abs(budget - total_cost)

if total_cost <= budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} USD left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} USD more.")
