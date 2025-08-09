while True:
    destination = input()
    if destination == "End":
        break

    budget = float(input())
    saved = 0.0

    while saved < budget:
        amount = float(input())
        saved += amount

    print(f"Going to {destination}!")
