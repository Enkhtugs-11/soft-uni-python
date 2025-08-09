favorite_book = input()

count = 0

while True:
    book = input()
    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count} books.")
        break
    if book == favorite_book:
        print(f"You checked {count} books and found it.")
        break
    count += 1
