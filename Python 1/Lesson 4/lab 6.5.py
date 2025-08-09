text = input()
sum = 0
for c in text:
    match c:
        case "a":
            sum += 1
        case "e":
            sum += 2
        case "i":
            sum += 3
        case "o":
            sum += 4
        case "u":
            sum += 5
print(sum)