nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())


material_cost = (nylon + 2) * 1.50 + (paint * 1.10) * 14.50 + thinner * 5.00 + 0.40
labor_cost = material_cost * 0.30 * hours

print(f"{material_cost + labor_cost:.2f}")