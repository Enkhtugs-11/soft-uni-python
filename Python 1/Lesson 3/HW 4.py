budget = int(input())
season = input()
fishermen = int(input())

if season == "Spring":
    rent_price = 3000
elif season == "Summer" or season == "Autumn":
    rent_price = 4200
elif season == "Winter":
    rent_price = 2600

if fishermen <= 6:
    rent_price *= 0.90
elif 7 <= fishermen <= 11:
    rent_price *= 0.85
else:
    rent_price *= 0.75

if fishermen % 2 == 0 and season != "Autumn":
    rent_price *= 0.95


difference = abs(budget - rent_price)

if budget >= rent_price:
    print(f"Yes! You have {difference:.2f} USD left.")
else:
    print(f"Not enough money! You need {difference:.2f} USD.")
