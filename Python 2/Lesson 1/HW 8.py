coffee = 0

while True:
    event = input()

    if event == "END":
        break

    if event.lower() in ["coding", "dog", "cat", "movie"]:
        if event.isupper():
            coffee += 2
        elif event.islower():
            coffee += 1

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
