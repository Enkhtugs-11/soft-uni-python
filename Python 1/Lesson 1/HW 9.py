length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_cm3 = length * width * height
volume_liters = volume_cm3 / 1000
usable_liters = volume_liters * (1 - percent / 100)

print(usable_liters)