budget = float(input())
flour_price_per_kg = float(input())

egg_price = 0.75 * flour_price_per_kg

milk_price_per_liter = 1.25 * flour_price_per_kg

milk_price_per_loaf = milk_price_per_liter * 0.25

loaf_cost = egg_price + flour_price_per_kg + milk_price_per_loaf

loaf_count = 0
colored_eggs = 0

while budget >= loaf_cost:
    budget -= loaf_cost
    loaf_count += 1
    colored_eggs += 3

    if loaf_count % 3 == 0:
        lost_eggs = loaf_count - 2
        colored_eggs -= lost_eggs
        if colored_eggs < 0:
            colored_eggs = 0

print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
