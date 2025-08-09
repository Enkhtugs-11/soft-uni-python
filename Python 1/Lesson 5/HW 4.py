goal = 10000
total_steps = 0

while True:
    command = input()

    if command == "Going home":
        steps_home = int(input())
        total_steps += steps_home
        break
    else:
        steps = int(command)
        total_steps += steps
        if total_steps >= goal:
            break

difference = abs(total_steps - goal)

if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
