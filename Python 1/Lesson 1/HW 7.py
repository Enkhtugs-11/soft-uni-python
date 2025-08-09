chicken_menu = int(input())
fish_menu = int(input())
vegatarian_menu = int(input())

chicken_price = 10.35
fish_price = 12.40
vegatarian_price = 8.15
delivery_price = 2.50

food_total = (chicken_menu * 10.35) + (fish_menu * 12.40) + (vegatarian_menu * 8.15)
dessert = food_total * 0.20
total = food_total + dessert + delivery_price

print(f"{total:.2f}")