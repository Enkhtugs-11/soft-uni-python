first = input()
second = input()

result = first

for i in range(len(first)):
    if first[i] != second[i]:
        result = result[:i] + second[i] + result[i+1:]
        print(result)
