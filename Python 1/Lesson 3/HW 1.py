screening_type = input().strip()
rows = int(input())
columns = int(input())

ticket_prices = {
    "Premiere": 12.00,
    "Normal": 7.50,
    "Discount": 5.00
}

total_seats = rows * columns

total_revenue = total_seats * ticket_prices[screening_type]

print(f"{total_revenue:.2f} USD")
