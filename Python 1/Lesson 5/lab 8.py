student_name = input()
current_grade = 1
fail_count = 0
total_grades = 0
grade_sum = 0.0

while current_grade <= 12:
    grade = float(input())

    if grade < 4.00:
        fail_count += 1
        if fail_count > 1:
            print(f"{student_name} has been excluded at {current_grade} grade")
            break
        continue

    grade_sum += grade
    total_grades += 1
    current_grade += 1

else:
    average = grade_sum / total_grades
    print(f"{student_name} graduated. Average grade: {average:.2f}")
