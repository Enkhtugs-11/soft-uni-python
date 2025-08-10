quantity = int(input())
days = int(input())

ornament_price = 2
ornament_points = 5

skirt_price = 5
skirt_points = 3

garland_price = 3
garland_points = 10

lights_price = 15
lights_points = 17

total_cost = 0
total_spirit = 0

for day in range(1, days + 1):
    bought_skirt_and_garland_today = False

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_cost += ornament_price * quantity
        total_spirit += ornament_points

    if day % 3 == 0:
        total_cost += (skirt_price + garland_price) * quantity
        total_spirit += skirt_points + garland_points
        bought_skirt_and_garland_today = True

    if day % 5 == 0:
        total_cost += lights_price * quantity
        total_spirit += lights_points

        if bought_skirt_and_garland_today:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        total_cost += skirt_price + garland_price + lights_price

    if day == days and day % 10 == 0:
        total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
