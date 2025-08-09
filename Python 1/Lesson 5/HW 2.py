max_poor_grades = int(input())

poor_grades = 0
total_grades = 0
sum_grades = 0
problems_solved = 0
last_problem = ""

while True:
    problem_name = input()

    if problem_name == "Enough":
        average_score = sum_grades / problems_solved
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {problems_solved}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())
    sum_grades += grade
    problems_solved += 1
    last_problem = problem_name

    if grade <= 4:
        poor_grades += 1
        if poor_grades >= max_poor_grades:
            print(f"You need a break, {poor_grades} poor grades.")
            break
