floors = int(input())
rooms = int(input())

for level in range(floors, 0, -1):
    for room in range(rooms):
        if level == floors:
            print(f"L{level}{room}", end = " ")
        elif level % 2 == 0:
            print(f"O{level}{room}", end = " ")
        else:
            print(f"A{level}{room}", end = " ")
    print()