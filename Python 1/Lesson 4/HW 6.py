actor_name = input()
initial_points = float(input())
n = int(input())

total_points = initial_points

for _ in range(n):
    assessor_name = input()
    assessor_points = float(input())
    total_points += (len(assessor_name) * assessor_points) / 2

    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")
