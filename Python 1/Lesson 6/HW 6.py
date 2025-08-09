total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie = input()
    if movie == "Finish":
        break

    free_seats = int(input())
    tickets_sold = 0

    while tickets_sold < free_seats:
        ticket_type = input()
        if ticket_type == "End":
            break


        tickets_sold += 1
        total_tickets += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

    fullness = tickets_sold / free_seats * 100
    print(f"{movie} - {fullness:.2f}% full.")

if total_tickets > 0:
    print(f"Total tickets: {total_tickets}")
    print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
    print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
    print(f"{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.")
else:
    print("No tickets were sold.")
