n1 = int(input())
n2 = int(input())
operator = input()

result = None

# Хуваах болон үлдэгдэл авах үед 0 шалгах
if operator == "/" or operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        if operator == "/":
            result = n1 / n2
            print(f"{n1} / {n2} = {result:.2f}")
        else:  # operator == "%"
            result = n1 % n2
            print(f"{n1} % {n2} = {result}")
else:
    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2

    parity = "even" if result % 2 == 0 else "odd"
    print(f"{n1} {operator} {n2} = {result} - {parity}")
