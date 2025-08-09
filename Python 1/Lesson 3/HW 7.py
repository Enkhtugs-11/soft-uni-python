month = input()
nights = int(input())

studio_price = 0
apartment_price = 0


if month in ["May", "October"]:
    studio_price = 50
    apartment_price = 65
elif month in ["June", "September"]:
    studio_price = 75.20
    apartment_price = 68.70
elif month in ["July", "August"]:
    studio_price = 76
    apartment_price = 77

if month in ["May", "October"]:
    if nights > 14:
        studio_price *= 0.70
    elif nights > 7:
        studio_price *= 0.95

elif month in ["June", "September"]:
    if nights > 14:
        studio_price *= 0.80


if nights > 14:
    apartment_price *= 0.90

total_studio = studio_price * nights
total_apartment = apartment_price * nights

print(f"Apartment: {total_apartment:.2f} USD.")
print(f"Studio: {total_studio:.2f} USD.")
