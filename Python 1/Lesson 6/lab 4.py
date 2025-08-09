start_num = int(input())
finish_num = int(input())
magic_num = int(input())
combinations = 0

is_found = False

for i in range(start_num, finish_num +1):
    for j in range(start_num, finish_num +1):
        combinations += 1

        if i + j == magic_num:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f"Combination N:{combinations} ({i} + {j} = {magic_num})")
else:
    print(f"{combinations} combinations - neither equals {magic_num}")