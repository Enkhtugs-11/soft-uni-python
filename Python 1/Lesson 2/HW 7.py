budget = float(input())
num_videocards = int(input())
num_cpus = int(input())
num_rams = int(input())

video_price = 250
total_video = num_videocards * video_price
cpu_price = total_video * 0.35
ram_price = total_video * 0.10

total_cost = (
    total_video +
    num_cpus * cpu_price +
    num_rams * ram_price
)

if num_videocards > num_cpus:
    total_cost *= 0.85

diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"You have {diff:.2f} USD left!")
else:
    print(f"Not enough money! You need {diff:.2f} USD more!")
