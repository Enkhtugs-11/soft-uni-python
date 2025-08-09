text = input()
sum = 0
vowel_nums = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5,
}
for c in text:
    sum += vowel_nums.get(c, 0)
print(sum)