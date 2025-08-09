groups_count = int(input())

total_climbers = 0

makalu = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(groups_count):
    group_size = int(input())
    total_climbers += group_size

    if group_size <= 5:
        makalu += group_size
    elif group_size <= 12:
        mont_blanc += group_size
    elif group_size <= 25:
        kilimanjaro += group_size
    elif group_size <= 40:
        k2 += group_size
    else:
        everest += group_size

print(f"{makalu / total_climbers * 100:.2f}%")
print(f"{mont_blanc / total_climbers * 100:.2f}%")
print(f"{kilimanjaro / total_climbers * 100:.2f}%")
print(f"{k2 / total_climbers * 100:.2f}%")
print(f"{everest / total_climbers * 100:.2f}%")
