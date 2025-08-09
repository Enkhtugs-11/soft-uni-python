width = int(input())
length = int(input())
height = int(input())

total_volume = width * length * height

used_volume = 0

while True:
    command = input()

    if command == "Done":
        break

    boxes = int(command)
    used_volume += boxes

    if used_volume >= total_volume:
        break

if used_volume >= total_volume:
    diff = used_volume - total_volume
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    free = total_volume - used_volume
    print(f"{free} Cubic meters left.")
