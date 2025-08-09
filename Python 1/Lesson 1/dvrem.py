# 1.Conditional(Нөхцөл шалгах) — if , elif, else
age = 18

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

    # ✨ if → гол нөхцөл
    # ✨ elif → өөр шалгах нөхцөл
    # ✨ else → дээрх аль нь ч биш бол

# 2. For loop (тоотой давталт)

for i in range(5):
    print("Hello", i)

    # Энэ нь дараахтай адил:
    # i = 0, 1, 2, 3, 4 → range(5) нь 0-с 4 хүртэл 5 удаа давтана
    #
# 3. While loop (нөхцөлтэй давталт)

count = 1
while count <= 3:
    print("Count is", count)
    count += 1
# while нь нөхцөл үнэн байвал давтана

# 4. Loop доторх Conditional

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
# Давталт бүрт if ашиглан even/odd шалгаж байна.

# Жишээ: 1-ээс 10 хүртэл тоонуудын нийлбэр олох
total = 0

for i in range(1, 11):
    total += i

print("Total sum:", total)

# Break ба Continue
for i in range(1, 10):
    if i == 5:
        break  # 5 дээр зогсоно
    print(i)

for i in range(1, 10):
    if i == 5:
        continue  # 5-г алгасна
    print(i)

# Хураангуй хүснэгт:

# | Төрөл                | Тайлбар                            |
# | -------------------- | ---------------------------------- |
# | `if`, `elif`, `else` | Нөхцөл шалгах                      |
# | `for`                | Давталт (range, list гэх мэт дээр) |
# | `while`              | Нөхцөл биелтэл давтана             |
# | `break`              | Давталтаас шууд гарах              |
# | `continue`           | Давталтын тухайн алхмыг алгасах    |
