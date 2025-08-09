budget = float(input())
season = input()

destination = ""
holiday_type = ""
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = budget * 0.30
        holiday_type = "Camp"
    elif season == "winter":
        money_spent = budget * 0.70
        holiday_type = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = budget * 0.40
        holiday_type = "Camp"
    elif season == "winter":
        money_spent = budget * 0.80
        holiday_type = "Hotel"

else:
    destination = "Europe"
    money_spent = budget * 0.90
    holiday_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{holiday_type} - {money_spent:.2f}")
