trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.60
doll_price = 3.00
bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

total_toys = puzzles + dolls + bears + minions + trucks
total_price = (
    puzzles * puzzle_price +
    dolls * doll_price +
    bears * bear_price +
    minions * minion_price +
    trucks * truck_price
)

if total_toys >= 50:
    total_price *= 0.75

total_price *= 0.90

diff = abs(total_price - trip_price)

if total_price >= trip_price:
    print(f"Yes! {diff:.2f} USD left.")
else:
    print(f"Not enough money! {diff:.2f} USD needed.")
