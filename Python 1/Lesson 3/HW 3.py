flower_type = input()
num_flowers = int(input())
budget = int(input())


prices = {
    "Roses": 5,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3,
    "Gladiolus": 2.50
}

flower_price = prices[flower_type]


if flower_type == "Roses" and num_flowers > 80:
    flower_price *= 0.90

elif flower_type == "Dahlias" and num_flowers > 90:
    flower_price *= 0.85

elif flower_type == "Tulips" and num_flowers > 80:
    flower_price *= 0.85

elif flower_type == "Narcissus" and num_flowers < 120:
    flower_price *= 1.15

elif flower_type == "Gladiolus" and num_flowers < 80:
    flower_price *= 1.20

total_price = flower_price * num_flowers

if total_price <= budget:
    remaining_budget = budget - total_price
    print(f"Hey, you have a great garden with {num_flowers} {flower_type} and {remaining_budget:.2f} USD left.")
else:
    needed_money = total_price - budget
    print(f"Not enough money, you need {needed_money:.2f} USD more.")
