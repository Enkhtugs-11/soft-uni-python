n = int(input())

total_sum = 0
total_count = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    sum_grades = 0
    for _ in range(n):
        grade = float(input())
        sum_grades += grade

    average = sum_grades / n
    print(f"{presentation_name} - {average:.2f}.")

    total_sum += average
    total_count += 1

if total_count > 0:
    final_average = total_sum / total_count
    print(f"Student's final assessment is {final_average:.2f}.")
else:
    print("No presentations were evaluated.")
