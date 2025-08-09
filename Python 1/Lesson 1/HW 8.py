fee = int(input())

sneakers = fee * 0.60
outfit = sneakers * 0.80
ball = outfit / 4
accessories = ball / 5

total = fee + sneakers + outfit + ball + accessories

print(f"{total:.2f}")