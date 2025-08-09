width = int(input())
length = int(input())

total_pieces = width * length

taken_pieces = 0

while True:
    command = input()

    if command == "STOP":
        break

    pieces = int(command)
    taken_pieces += pieces

    if taken_pieces >= total_pieces:
        break

if taken_pieces >= total_pieces:
    needed = taken_pieces - total_pieces
    print(f"No more cake left! You need {needed} pieces more.")
else:
    left = total_pieces - taken_pieces
    print(f"{left} pieces are left.")
