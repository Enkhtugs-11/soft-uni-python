import math

figure = input()

if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    length = float(input())
    width = float(input())
    area = length * width
elif figure == "circle":
    radius = float(input())
    area = math.pi * (radius ** 2)
elif figure == "triangle":
    base = float(input())
    height = float(input())
    area = (base * height) / 2
else:
    area = None

if area is not None:
    print(f"{area:.3f}")
else:
    print("Invalid figure type.")
