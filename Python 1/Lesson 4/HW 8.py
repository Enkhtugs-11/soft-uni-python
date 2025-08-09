tournaments = int(input())
initial_points = int(input())

points_earned = 0
wins = 0

for _ in range(tournaments):
    result = input()
    if result == "W":
        points_earned += 2000
        wins += 1
    elif result == "F":
        points_earned += 1200
    elif result == "SF":
        points_earned += 720

total_points = initial_points + points_earned
average_points = points_earned // tournaments
win_percentage = (wins / tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{win_percentage:.2f}%")
